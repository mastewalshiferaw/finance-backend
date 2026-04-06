# Finance Data Processing Backend

A secure, role-based REST API designed for financial record management, featuring JWT authentication, CRUD operations, and aggregated dashboard analytics.

## Features
- **User Roles:** Role-Based Access Control (Admin, Analyst, Viewer).
- **Authentication:** Stateless JWT Authentication via `simplejwt`.
- **Financial Management:** Secure CRUD operations for income and expense transactions.
- **Aggregated Analytics:** Dashboard Summary API for net balance, income/expense totals, and record counts.
- **Production-Ready:** Deployed with PostgreSQL (Neon) and WhiteNoise for static file management.

## API Documentation & Testing
The API is live at: `https://finance-backend-i53x.onrender.com/`

### Key Endpoints:
| Method | Endpoint | Description | Permission |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/register/` | Register a new user | Public |
| `POST` | `/api/token/` | Get JWT Access Token | Public |
| `GET` | `/api/records/transactions/` | List/View Transactions | Authenticated |
| `POST` | `/api/records/transactions/` | Create new transaction | Admin |
| `GET` | `/api/records/summary/` | Get dashboard summary | Analyst, Admin |

## Local Setup
1. **Clone & Install:**
   ```bash
   git clone https://github.com/mastewalshiferaw/finance-backend
   cd finance-backend
   pip install -r requirements.txt

⚙️ Environment Variables

Set the following variables (in .env or your system environment):

SECRET_KEY=your_django_secret_key
DATABASE_URL=your_database_connection_string
ADMIN_USER=admin_username
ADMIN_EMAIL=admin_email
ADMIN_PASS=admin_password

🚀 Run the Project
python manage.py migrate
python manage.py setup_admin
python manage.py runserver

🔧 Technical Highlights
Security: Implemented custom permission classes using Django REST Framework to enforce role-based access control.
Precision: Used DecimalField for financial data to avoid floating-point inaccuracies.
Performance: Leveraged database-level aggregations (Sum, Count) for scalable dashboard metrics.
Automation: Created a custom management command (setup_admin) for secure, environment-based admin initialization.
Stateless Authentication: Used JWT via djangorestframework-simplejwt for secure and scalable authentication.
💡 Notes
Ensure environment variables are properly configured before running the server.
The setup_admin command automatically creates an admin user during deployment.