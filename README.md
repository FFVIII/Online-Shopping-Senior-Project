# Shopping Cart Application

A Python Flask-based e-commerce shopping cart application with user authentication and product management.

## Features

- 🛒 **Shopping Cart** - Add, remove, and manage products in cart
- 👤 **User Authentication** - Register and login with secure password hashing (bcrypt)
- 📱 **Product Categories** - Browse products by category (Desktop, Laptop, Cellphone)
- 🔍 **Search Functionality** - Search products by name
- 💳 **Payment Page** - Integrated payment interface
- 📊 **Product Management** - View detailed product information

## Tech Stack

- **Backend:** Flask (Python web framework)
- **Database:** MySQL
- **Authentication:** Bcrypt password hashing
- **Frontend:** HTML/CSS/JavaScript (Jinja2 templates)

## Requirements

- Python 3.7+
- MySQL Server
- pip (Python package manager)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/shopping-cart.git
cd shopping-cart
```

### 2. Install Python Dependencies
```bash
pip install flask flask-mysql pymysql bcrypt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root:
```
MYSQL_USER=root
MYSQL_PASSWORD=1234
MYSQL_DB=online
MYSQL_HOST=localhost
FLASK_SECRET_KEY=your_secure_secret_key_here
```

### 4. Set Up Database

Make sure MySQL is running, then execute the SQL setup:

```bash
mysql -u root -p1234 -h localhost < online.sql
```

Or manually run the SQL file:
```bash
mysql -u root -p
# Enter password: 1234
# Then run: source online.sql;
```

## Running the Application

```bash
python main.py
```

The application will start on `http://127.0.0.1:5000`

**Default Port:** 5000  
**Debug Mode:** Enabled (auto-reload on code changes)

## Project Structure

```
shopping-cart/
├── main.py                 # Main Flask application
├── online.sql             # Database schema and sample data
├── static/                # Static files (CSS, JS, images)
├── templates/             # HTML templates
│   ├── products.html      # All products page
│   ├── desktop.html       # Desktop products
│   ├── laptop.html        # Laptop products
│   ├── cellphone.html     # Cellphone products
│   ├── cart.html          # Shopping cart
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── pay.html           # Payment page
│   ├── alldetail.html     # Product details
│   ├── pcdetail.html      # Desktop details
│   ├── laptopdetail.html  # Laptop details
│   └── cellphonedetail.html # Cellphone details
└── README.md              # This file
```

## Usage

### Browse Products
1. Navigate to `http://127.0.0.1:5000/` to view all products
2. Use category links to filter by product type
3. Click on a product for details

### User Registration
1. Click "Register" link
2. Enter name, email, and password
3. Password will be securely hashed with bcrypt

### Shopping
1. Add items to cart by selecting quantity and clicking "Add to Cart"
2. View cart at `http://127.0.0.1:5000/cart`
3. Remove items or clear entire cart
4. Proceed to checkout/payment

### Search
1. Use the search bar to find products by name
2. Results display matching products

## Database Schema

### Users Table
```sql
- id (INT, Primary Key)
- name (VARCHAR 128)
- email (VARCHAR 45)
- password (VARCHAR 999, hashed)
```

### Products Table
```sql
- id (INT, Primary Key)
- name (VARCHAR 255)
- code (VARCHAR 255)
- image (TEXT)
- price (INT)
```

## API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page (all products) |
| `/desktop` | GET | Desktop products |
| `/laptop` | GET | Laptop products |
| `/cellphone` | GET | Cellphone products |
| `/alldetail/<id>` | GET | Product details |
| `/pcdetail/<id>` | GET | Desktop product details |
| `/laptopdetail/<id>` | GET | Laptop product details |
| `/cellphonedetail/<id>` | GET | Cellphone product details |
| `/cart` | GET | Shopping cart page |
| `/add` | POST | Add product to cart |
| `/delete/<code>` | GET | Remove product from cart |
| `/empty` | GET | Clear entire cart |
| `/search` or `/result` | POST | Search products |
| `/login` | GET, POST | User login |
| `/logout` | GET, POST | User logout |
| `/register` | GET, POST | User registration |
| `/pay` | GET | Payment page |

## Session Management

The application uses Flask sessions to manage:
- User authentication (`session['name']`, `session['email']`)
- Shopping cart items (`session['cart_item']`)
- Cart totals (`session['all_total_price']`, `session['all_total_quantity']`)

## Sample Data

The database includes 24 sample products:
- 8 Desktop computers (IDs 1-8)
- 8 Laptops (IDs 9-16)
- 8 Cellphones (IDs 17-24)

Each product has a demo price of 2000.

## Security Notes

⚠️ **Important:** This is a student project. Before deploying to production:
- Use environment variables for all sensitive credentials (see .env setup)
- Implement parameterized queries for all database operations
- Add HTTPS/SSL encryption
- Validate and sanitize all user inputs
- Implement CSRF protection
- Use production-grade session management
- Add comprehensive error handling
- Implement logging
- Use a production WSGI server (not Flask's development server)

## Future Improvements

- [ ] Product pagination
- [ ] Advanced filtering and sorting
- [ ] Real payment gateway integration
- [ ] Order history
- [ ] Admin dashboard
- [ ] Product reviews and ratings
- [ ] Wishlist feature
- [ ] Email notifications
- [ ] Inventory management
- [ ] Unit tests

## Troubleshooting

### MySQL Connection Error
- Ensure MySQL is running
- Verify credentials in `.env` match your MySQL setup
- Check `MYSQL_HOST` is set to `localhost` or correct IP

### Import Error: No module named 'flask'
```bash
pip install flask flask-mysql pymysql bcrypt
```

### Port Already in Use
Change the port in `main.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change 5001 to desired port
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss proposed changes.

## License

This project is open source and available under the MIT License.

## Author

Senior Project - Shopping Cart Application

---

**Last Updated:** 2026-06-07  
**Python Version:** 3.7+  
**Flask Version:** Compatible with 2.0+
