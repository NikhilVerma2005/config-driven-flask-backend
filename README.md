# 🚀 Config-Driven Flask Backend (Dockerized & Deployed)

A **production-ready Flask backend** demonstrating secure authentication, role-based authorization, environment-driven configuration, and real cloud deployment using Docker and Gunicorn.

> This project focuses on **backend fundamentals + deployment realism**, not just CRUD endpoints.

---

## 🔧 Tech Stack

- **Backend:** Flask (Blueprint architecture)
- **Auth:** Session-based authentication (signed cookies)
- **Database:** SQLite (configurable, production-switchable)
- **ORM:** SQLAlchemy
- **Security:** Password hashing, protected routes, role checks
- **Server:** Gunicorn (WSGI)
- **Containerization:** Docker
- **Deployment:** Render (Free Tier)
- **Config Management:** Environment variables + TOML configs

---

## ✨ Key Features

- 🔐 **Secure Authentication**
  - Login / Logout
  - Password hashing & verification
  - Session-based authentication using Flask signed cookies

- 🛂 **Authorization**
  - Protected routes (`/dashboard`)
  - Role-based access control (`/admin`)

- ⚙️ **Config-Driven Architecture**
  - Environment-based configuration (`APP_ENV`)
  - Secrets via environment variables (`SECRET_KEY`)
  - Database URL configurable per environment

- 🐳 **Production-Ready Deployment**
  - Dockerized application
  - Gunicorn WSGI server
  - Deployed on Render with cold-start awareness

- 🧠 **Real-World Constraints Handled**
  - No shell access on free tier
  - Safe database bootstrapping
  - Cold start behavior understood and handled

---

## 🗂 Project Structure

```
.
├── app.py                 # Flask app entry point
├── wsgi.py                # Gunicorn entry point
├── auth/
│   ├── routes.py          # Auth routes (login, logout, dashboard)
│   └── decorators.py      # login_required, role_required
├── db/
│   ├── database.py        # SQLAlchemy engine & session
│   └── models.py          # User model
├── utils/
│   ├── security.py        # Password hashing utilities
│   └── db_session.py      # DB session helper
├── config/
│   ├── dev.toml           # Development config
│   └── prod.toml          # Production config
├── scripts/
│   └── create_user.py     # Local admin creation (non-prod)
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🔑 Authentication Flow (High Level)

1. User logs in via `/login`
2. Credentials are verified using hashed passwords
3. Flask creates a **signed session cookie**
4. Protected routes validate session presence
5. Logout clears session and invalidates cookie

---

## 🌍 Live Deployment

**Base URL:**
```
https://config-driven-flask-backend.onrender.com
```

### Health Check
```bash
curl https://config-driven-flask-backend.onrender.com/health
```

Expected:
```json
{"status":"ok"}
```

---

## 🧪 API Testing (Sample)

### Login
```bash
curl -X POST https://config-driven-flask-backend.onrender.com/login \
-H "Content-Type: application/json" \
-d '{"username":"nik","password":"pass123"}'
```

### Protected Dashboard
```bash
curl https://config-driven-flask-backend.onrender.com/dashboard
```

Returns `Unauthorized` if not logged in.

---

## 🚧 Free-Tier Deployment Notes

- Render free tier suspends inactive services
- First request after inactivity may be slow (cold start)
- SQLite database may reset on container restart
- Admin user is safely bootstrapped if DB is empty

---

## 🔐 Security Considerations

- Secrets are never hardcoded
- `SECRET_KEY` is injected via environment variables
- Passwords are stored as hashes only
- Unauthorized access is strictly blocked

---

## 🧠 What This Project Demonstrates

- Backend architecture & separation of concerns
- Authentication & session management
- Real production deployment challenges
- Docker + Gunicorn usage
- Debugging real cloud issues
- Security-first thinking

---

## 👨‍💻 Author

**Nikhil**  
Engineering Student | Backend & Systems Enthusiast

- GitHub: [@NikhilVerma2005](https://github.com/NikhilVerma2005)
- LinkedIn: [Nikhil Verma](https://www.linkedin.com/in/nikhil-verma-5767b3290/)