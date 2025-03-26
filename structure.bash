flask-ecommerce
│── static                   # Static files (CSS, JS, Images)
│   ├── css                  # CSS stylesheets
│   ├── js                   # JavaScript files
│   ├── images               # Product images
│── templates                # HTML templates
│   ├── base.html             # Main template (extends other pages)
│   ├── index.html            # Home page (product listings)
│   ├── product.html          # Product details page
│   ├── cart.html             # Shopping cart page
│   ├── checkout.html         # Checkout page
│── models                   # Database models
│   ├── product.py            # Product model
│   ├── user.py               # User model
│   ├── order.py              # Order model
│── routes                   # Routes for different functionalities
│   ├── auth.py               # User authentication (loginregister)
│   ├── product_routes.py     # Product-related routes
│   ├── cart_routes.py        # Cart and checkout routes
│── forms                    # Forms for authentication, checkout, etc.
│   ├── login_form.py         # Login form
│   ├── register_form.py      # Registration form
│── database.py               # Database setup
│── app.py                    # Main Flask application file
│── config.py                 # Configuration file
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation
