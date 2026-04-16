# 🏛️ ForgeCart | BackForge Hackathon Project

![BackForge Banner](https://img.shields.io/badge/BackForge-2026-f97316?style=for-the-badge&logo=github)
![Frontend Status](https://img.shields.io/badge/Frontend-Static%20Complete-success?style=for-the-badge)

Welcome to the **ForgeCart** frontend repository. This project is a specialized "Forgeable" frontend designed for the **BackForge Hackathon**. 

### 🏆 The Challenge
Participants are provided with this premium, static frontend and are tasked with **"Forging the Backend"**. Your goal is to transform this static experience into a fully functional E-commerce platform by building the API, database, and integration layer.

---

## 🛠️ 10 Key Features to Forge

To successfully complete the BackForge challenge, participants must implement the following 10 features:

1.  **User Authentication System**: Implement secure Sign Up and Login logic (using JWT or Sessions) including password hashing and session management.
2.  **Dynamic Product Catalog**: Replace static HTML cards with a dynamic retrieval system that fetches product data from your database.
3.  **Search API Integration**: Enable the search bar to query the database and return relevant results in real-time.
4.  **Multi-Category Filtering**: Implement backend logic to filter products by category (Apparel, Digital, Accessories) via API endpoints.
5.  **Product Detail Retrieval**: Create a dynamic product page that loads specific item data based on unique identifiers (IDs).
6.  **Persistent Shopping Cart**: Build a system that saves cart items to the database or local storage, ensuring they persist across user sessions.
7.  **Order Placement Engine**: Process the checkout form and transition cart items into a permanent "Order" record in the database.
8.  **Personalized Order History**: Develop a secure dashboard for users to view their past orders, including status and timestamps.
9.  **Inventory State Management**: Implement logic to track stock levels and reflect "Out of Stock" states on the frontend when inventory is depleted.
10. **Secure Form Handling**: Implement robust server-side validation and sanitization for all user inputs (Auth, Search, and Checkout).

---

## 🚀 Tech Stack (Frontend)

- **Style**: Premium Glassmorphism UI (Vanilla CSS).
- **Typography**: Outfit & Inter (Google Fonts).
- **Icons**: Font Awesome 6.4.0.
- **Structure**: Semantic HTML5 with a focus on ease of integration.

---

## 📸 Project Layout

| Page | Description |
| :--- | :--- |
| `index.html` | Hero section, Product Grid, Search, and Filters. |
| `product.html` | Detailed product specifications and "Deploy to Cart" logic. |
| `cart.html` | Summary of selected items and total calculations. |
| `checkout.html` | Shipping and Payment information gathering. |
| `orders.html` | Dashboard for viewing previous purchases. |
| `login.html` | Entry point for returning users. |
| `register.html` | Onboarding flow for new participants. |

---

## 📂 Getting Started

1. **Clone the UI**:
   ```bash
   git clone https://github.com/backforgenmiet/Management-E-Commerce-Web-2.git
   ```
2. **Analyze the DOM**: Open the HTML files to identify the classes and IDs where your dynamic data will be injected.
3. **Forge the Backend**: Build your server, connect your database, and let the forging begin!

---

Developed for the **BackForge Hackathon**. *The frontend is the canvas; your backend is the masterpiece.*