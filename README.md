Library Management System API

This project is a RESTful API for a Library Management System built with Django REST Framework (DRF). It allows users to register, log in, borrow and return books, and manage authors and transactions.

Features:

User authentication (registration, login)

Book and author management

Borrowing and returning books

Transaction tracking

Author

Developer: Yolanda Mokwena mookie.mokwena@gmail.com

Installation & Setup

Prerequisites

Ensure you have the following installed:

Python 3.x

Django

Django REST Framework

Django REST Framework Token Authentication

Installation & Setup:

git clone https://github.com/YolandaM16/Library_Management_System_API.git
cd project_directory
django-admin manage.py startproject library_management_system_api
python3 manage.py startapp library_catalog
Create a virtual environment and activate it:
pipenv shell
Apply migrations:
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

API Endpoints

Authentication

Register a User
*POST* http://127.0.0.1:8000/api/register/

{
  "username": "john",
  "email": "johndoe@gmail.com",
  "password": "john57"
}

Login 
*POST* http://127.0.0.1:8000/api/login/

{
    "username": "john",
    "password": "john57"
}

Profile
*GET* http://127.0.0.1:8000/api/profile/ (Admin only)

Author:

Author Detail
*POST* http://127.0.0.1:8000/api/authors/<id>/ (Admin only)

{
    "name": 5
}

Author List
*GET* http://127.0.0.1:8000/api/authors/ (Admin only)

Books:
*GET* http://127.0.0.1:8000/api/book/

*POST* http://127.0.0.1:8000/api/book/ (Admin only)

*POST* http://127.0.0.1:8000/api/checkout/
{
    "book": 5
}

Transaction:
*GET* http://127.0.0.1:8000/api/transactions/

Testing with Postman:

1. Set up Postman and create a collection.

2. Register a new user and obtain an authentication token.

3. Use the token in the Authorization header for all authenticated requests:

Authorization: Token {{auth_token}}

Test various endpoints as documented above.