# Finance Data Processing Backend
A secure API for managing financial records with Role-Based Access Control.

## Features
- User roles (Admin, Analyst, Viewer)
- JWT Authentication
- Transaction CRUD
- Aggregated Dashboard Analytics

## Setup
1. `pip install -r requirements.txt`
2. `python manage.py migrate`
3. `python manage.py createsuperuser`
4. `python manage.py runserver`