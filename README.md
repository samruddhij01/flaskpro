FlaskPro

A Flask-based web application for user registration, authentication, and data management. Users can register, log in, view their dashboard, update their information, and browse stored data through a set of simple web pages.

Features
User Registration – New users can sign up via the registration page.
Login / Logout – Secure authentication for registered users.
Dashboard – A personalized dashboard view after login.
Update Information – Users can edit and update their saved details.
View Data – Browse stored records in the database.
About & Contact Pages – Static informational pages for the app.
Tech Stack
Backend: Python (Flask)
Database: SQLite (pro.db, login.db)
Frontend: HTML, CSS (Jinja2 templates)
Project Structure
flaskpro/
├── static/            # CSS, JS, images
├── templates/         # HTML templates
│   ├── about.html
│   ├── contact.html
│   ├── dashboard.html
│   ├── home.html
│   ├── login.html
│   ├── nav.html
│   ├── reg.html
│   ├── test.html
│   ├── test1.html
│   ├── update.html
│   └── viewdata.html
├── app.py             # Main Flask application
├── db.py              # Database connection/setup logic
├── design.py          # App design/layout helper
├── redirect.py         # Redirect handling logic
├── test.py            # Test script
├── url.py             # URL routing logic
├── login.db           # SQLite database for login/auth
├── pro.db             # SQLite database for project data
└── .gitattributes
Getting Started
Prerequisites
Python 3.x installed
pip (Python package manager)
Installation
Clone the repository
bash
   git clone https://github.com/samruddhij01/flaskpro.git
   cd flaskpro
Install Flask
bash
   pip install flask
Run the application
bash
   python app.py
Open your browser and go to
   http://127.0.0.1:5000/
Usage
Visit the Home page to explore the app.
Register a new account from the registration page.
Login with your credentials to access the dashboard.
View your Dashboard and stored data.
Update your information whenever needed.
Check out the About and Contact pages for more details.
Future Improvements
Add password hashing for secure authentication
Add delete functionality for user records
Improve UI with a CSS framework (Bootstrap/Tailwind)
Add form validation and error handling
Migrate to a more scalable database (PostgreSQL/MySQL)
Author

Samruddhi Jadhav

License

This project is open source and available for personal and educational use.

Content
1788600906631_ecommerce
