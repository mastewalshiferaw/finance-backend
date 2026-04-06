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

## ⚙️ Environment Variables
Configure the following variables in a `.env` file or your system environment before running the server:

| Variable | Description |
| :--- | :--- |
| `SECRET_KEY` | Your Django secret key for cryptographic signing. |
| `DATABASE_URL` | Connection string for your PostgreSQL or SQLite database. |
| `ADMIN_USER` | Username for the initial automated admin account. |
| `ADMIN_EMAIL` | Email address for the initial admin account. |
| `ADMIN_PASS` | Secure password for the initial admin account. |

---

## 🚀 Running the Project
After cloning the repository and installing the requirements, run the following commands to start the project:

```bash
# 1. Apply database migrations
python manage.py migrate

# 2. Initialize the admin account using your environment variables
python manage.py setup_admin

# 3. Start the development server
python manage.py runserver

🛠 Technical Highlights
Security: Enforced granular access control using custom DRF Permission Classes for robust Role-Based Access Control (RBAC).
Precision: Implemented DecimalField for all monetary transactions to eliminate floating-point arithmetic errors.
Performance: Utilized database-level aggregation (Sum, Count) for the dashboard summary, ensuring fast response times even as data grows.
Automation: Developed a custom Django management command (setup_admin) to facilitate seamless, secure environment-based deployments.
Scalability: Leveraged JWT (JSON Web Tokens) via simplejwt for a stateless, decoupled authentication architecture.

💡 Notes
Ensure all environment variables are properly configured before running the server or the setup command.
The setup_admin command automatically creates your initial admin user during deployment based on your environment variables.