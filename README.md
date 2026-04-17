# 🛒 ForgeCart – E-Commerce Web Application

## 📌 Overview

**ForgeCart** is a full-stack e-commerce web application built with **Flask** and **MySQL**, developed for the **BackForge Hackathon**.

It provides a complete **storefront with working authentication**, allowing users to register, log in, browse products, manage their cart, and place orders — all backed by a real database.

This project is ideal for:

* Hackathon participants building full-stack apps
* Backend developers learning Flask + MySQL integration
* Teams looking for a production-ready e-commerce foundation

---

## 🚀 Key Highlights

* 🔐 **Working Authentication** — Register, Login, Logout with hashed passwords
* 🗄️ **MySQL Database** — User data stored securely in MySQL via SQLAlchemy
* 🔒 **Password Hashing** — Bcrypt-based secure password storage
* 🍪 **Session Management** — Flask-Login for persistent user sessions
* 🎨 **Modern UI/UX** — Glassmorphism design with responsive layout
* 📱 **Fully Responsive** — Works on desktop, tablet, and mobile
* ⚙️ **Environment Variables** — Credentials managed securely via `.env`

---

## ⚙️ Backend Workflow

### Authentication Flow
1. **Sign Up:** User enters name, email, and password. Password is hashed using `bcrypt` and stored in the `user` table.
2. **Login:** User credentials are verified against the database. If successful, `Flask-Login` creates a secure session.
3. **Session Management:** Users remain logged in across pages until they explicitly log out.

### Order & Checkout Workflow
1. **Cart Management:** Users can add products to their cart from the dashboard. The system checks if the item exists and increments quantity or creates a new entry in the `cart_item` table.
2. **Checkout:** The `/checkout.html` route ensures the user is logged in and has items in their cart. It calculates the subtotal dynamically.
3. **Execution (Order Placement):** Upon "Authorizing & Compiling Order," the backend:
    * Generates a new record in the `order` table.
    * Transfers cart items to the `order_item` table for permanent record-keeping.
    * Flushes the `cart_item` table for that specific user.
4. **Execution Logs (Orders):** The `/orders.html` page queries the database for all orders associated with the logged-in user, displaying them in reverse chronological order.

---

## 🏗️ System Architecture

ForgeCart follows a **Flask multi-page architecture** with MySQL backend:

### 🔹 Architecture Layers

**1. Frontend Layer**

* HTML5 + Jinja2 Templates
* CSS3 with Glassmorphism design
* Font Awesome 6.4.0 (icons)
* Google Fonts (Outfit, Inter)

**2. Backend Layer (Flask)**

* Route handling & page rendering
* User authentication (register, login, logout)
* Session management with Flask-Login
* Password hashing with Flask-Bcrypt
* Protected routes (e.g., Orders page)

**3. Data Layer (MySQL)**

* MySQL 8.0 database (`forgecart`)
* SQLAlchemy ORM for database operations
* PyMySQL driver for MySQL connectivity
* Auto table creation on app startup

---

## 🛍️ Features & Modules

### 🔐 Authentication (✅ Fully Working)

* **Registration** — Name, email, password with confirmation
* **Login** — Email/password authentication against MySQL
* **Logout** — Session clearing and redirect
* **Password Security** — Bcrypt hashing (never stored in plain text)
* **Duplicate Prevention** — Email uniqueness check on registration
* **Protected Routes** — Orders page requires login
* **Error Handling** — User-friendly error messages on forms

---

### 🏠 Landing & Product Listing

* Hero section with call-to-action
* Product grid layout with images
* Search bar UI
* Category filters (All, Apparel, Digital, Accessories)
* Featured products display

---

### 📦 Product Details

* Product image gallery
* Pricing section
* Specifications
* Add to Cart & Buy Now buttons

---

### 🛒 Cart

* Item listing with product details
* Quantity controls
* Remove item option
* Price summary with totals
* Checkout button

---

### 💳 Checkout

* Shipping information form
* Payment details form
* Order summary review
* Place Order button

---

### 📜 Orders (🔒 Login Required)

* Order history display
* Status tracking
* Timestamps
* Order summary details

---

## 🎨 UI/UX Design

### Design Principles

* Glassmorphism UI with frosted-glass effects
* Modern dark theme storefront
* Clean and minimal navigation
* Mobile-first responsiveness

### Styling

* Dark background with gradient accents
* Orange highlight colors
* Rounded components with soft shadows
* Hover effects and smooth transitions

### Interactions

* Smooth CSS transitions
* Hover animations on cards and buttons
* Interactive form styling with validation
* Error/success message displays

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.13, Flask 3.0 |
| **Database** | MySQL 8.0 |
| **ORM** | Flask-SQLAlchemy |
| **DB Driver** | PyMySQL |
| **Auth** | Flask-Login |
| **Hashing** | Flask-Bcrypt |
| **Config** | python-dotenv |
| **Frontend** | HTML5, CSS3, Jinja2 |
| **Icons** | Font Awesome 6.4.0 |
| **Fonts** | Google Fonts (Outfit, Inter) |

---

## 📁 Project Structure

```
ForgeCart/
│
├── app.py                # Main Flask application (routes, auth, DB)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (gitignored)
├── .env.example          # Template for environment config
├── .gitignore            # Git ignore rules
├── LICENSE               # Project license
├── README.md             # This file
│
├── templates/            # Jinja2 HTML templates
│   ├── index.html        # Landing / Product Listing
│   ├── product.html      # Product Details
│   ├── cart.html         # Cart Page
│   ├── checkout.html     # Checkout Flow
│   ├── orders.html       # Order History (login required)
│   ├── login.html        # Login Page
│   └── register.html     # Registration Page
│
└── static/               # Static assets
    ├── css/
    │   └── styles.css    # Global stylesheet
    └── assets/
        └── images/       # Product images
```

---

## ⚡ Getting Started

### Prerequisites

* **Python 3.10+** installed
* **MySQL 8.0** installed and running
* **pip** (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/prathamesh-lang/Management-E-Commerce-Web-2.git
cd Management-E-Commerce-Web-2
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up MySQL Database

Open your MySQL client and run:

```sql
CREATE DATABASE IF NOT EXISTS forgecart;
```

### 4. Configure Environment Variables

Copy the example file and update with your credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```env
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_DB=forgecart
SECRET_KEY=your_secret_key_here
```

### 5. Run the Application

```bash
python app.py
```

The app will:
1. Auto-create the `user` table in MySQL
2. Start the Flask dev server at **http://127.0.0.1:5000**

---

## 🗄️ Database Schema

### `user` Table

| Column | Type | Constraints |
|--------|------|-------------|
| `id` | INT | Primary Key, Auto Increment |
| `name` | VARCHAR(100) | NOT NULL |
| `email` | VARCHAR(120) | UNIQUE, NOT NULL |
| `password` | VARCHAR(60) | NOT NULL (Bcrypt hash) |

---

## 🔐 Authentication Flow

```
Register:
  User → Fill Form → POST /register.html → Validate → Hash Password → Save to MySQL → Auto Login → Redirect Home

Login:
  User → Fill Form → POST /login.html → Query MySQL → Verify Bcrypt Hash → Create Session → Redirect Home

Logout:
  User → GET /logout → Clear Session → Redirect Home

Protected Route:
  User → GET /orders.html → Check Session → If Not Logged In → Redirect to Login
```

---

## 📱 Responsiveness

ForgeCart is optimized for:

* 💻 Desktop
* 📱 Tablet
* 📲 Mobile

Built using:

* CSS Grid & Flexbox
* Mobile-first media queries
* Responsive typography

---

## 🔮 Future Enhancements

* ~~Backend API integration~~ ✅ Done
* ~~Session authentication~~ ✅ Done
* Dynamic product catalog from database
* Real-time search functionality
* Advanced filtering logic
* Persistent cart (database-backed)
* Payment gateway integration (Razorpay/Stripe)
* Order & inventory management
* Wishlist system
* Reviews & ratings
* Admin dashboard
* REST API endpoints

---

## 🤝 Contribution

This project is part of the **BackForge Hackathon ecosystem**.
Feel free to fork, extend, and integrate your own features.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📜 License

This project is open for educational and hackathon use.

---

💡 *Build fast. Ship faster. Forge better.*
