import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

load_dotenv()

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_secret')
DB_USER = os.getenv('MYSQL_USER', 'root')
DB_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
DB_HOST = os.getenv('MYSQL_HOST', 'localhost')
DB_NAME = os.getenv('MYSQL_DB', 'forgecart')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    product_image = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, default=1)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.Text, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    date_ordered = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/cart.html')
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    subtotal = sum(item.product_price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal)

@app.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    product_name = request.form.get('product_name')
    product_price = float(request.form.get('product_price').replace('$', ''))
    product_image = request.form.get('product_image')
    
    existing_item = CartItem.query.filter_by(user_id=current_user.id, product_name=product_name).first()
    if existing_item:
        existing_item.quantity += 1
    else:
        new_item = CartItem(user_id=current_user.id, product_name=product_name, product_price=product_price, product_image=product_image)
        db.session.add(new_item)
    db.session.commit()
    flash('Item added to cart')
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:item_id>', methods=['POST'])
@login_required
def remove_from_cart(item_id):
    item = CartItem.query.get_or_404(item_id)
    if item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('cart'))

@app.route('/checkout.html')
@login_required
def checkout():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash('Your cart is empty.')
        return redirect(url_for('cart'))
    subtotal = sum(item.product_price * item.quantity for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, subtotal=subtotal)

@app.route('/place_order', methods=['POST'])
@login_required
def place_order():
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    address = request.form.get('address')
    
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash('Cart is empty!')
        return redirect(url_for('index'))
    
    subtotal = sum(item.product_price * item.quantity for item in cart_items)
    
    new_order = Order(user_id=current_user.id, fullname=fullname, email=email, address=address, total_price=subtotal)
    db.session.add(new_order)
    db.session.flush() # To get the order ID
    
    for item in cart_items:
        order_item = OrderItem(order_id=new_order.id, product_name=item.product_name, product_price=item.product_price, quantity=item.quantity)
        db.session.add(order_item)
        db.session.delete(item) # Clear cart
        
    db.session.commit()
    flash('Order placed successfully!')
    return redirect(url_for('orders'))

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            error = 'Login Unsuccessful. Please check email and password'
    return render_template('login.html', error=error)

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            error = 'Passwords do not match!'
        else:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                error = 'Email already registered. Please login.'
            else:
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                user = User(name=name, email=email, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('index'))
    return render_template('register.html', error=error)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/orders.html')
@login_required
def orders():
    user_orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.date_ordered.desc()).all()
    return render_template('orders.html', orders=user_orders)

@app.route('/product.html')
def product():
    return render_template('product.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
