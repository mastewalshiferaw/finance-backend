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
Environment Variables:
Set the following variables (in .env or your system environment):
SECRET_KEY: Your Django secret key.
DATABASE_URL: Connection string for PostgreSQL/SQLite.
ADMIN_USER: Username for the initial admin account.
ADMIN_EMAIL: Email for the initial admin account.
ADMIN_PASS: Password for the initial admin account.
Run the Project:
code
Bash
python manage.py migrate
python manage.py setup_admin
python manage.py runserver
Technical Highlights
Security: Implemented custom DRF Permission Classes to enforce role-based access.
Precision: Used DecimalField for currency handling to prevent floating-point errors.
Performance: Used database-level aggregation (Sum/Count) for dashboard metrics to ensure scalability.
Automation: Created a custom management command (setup_admin) for secure, environment-based admin initialization during deployment.
Stateless Authentication: Used JSON Web Tokens (JWT) via simplejwt for secure, scalable authentication.
💡 Notes
Ensure environment variables are properly configured before running the server.
The setup_admin command automatically creates an admin user during deployment based on your environment variables.