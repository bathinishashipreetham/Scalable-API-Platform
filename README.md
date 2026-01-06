# 🚀 Scalable API Platform

A **production-grade backend system** built with **FastAPI**, designed using **FAANG-level engineering practices** including clean architecture, JWT authentication, CI/CD, Dockerization, and testability.

> Built to demonstrate real-world backend engineering skills for SDE / Backend roles.

---------
## 📸 Project Demo

<img width="1085" height="962" alt="demo" src="https://github.com/user-attachments/assets/764017a2-1fd0-42e9-b02c-95f7391567bd" />


----------
## ✨ Features

- ✅ FastAPI with Pydantic v2
- 🔐 JWT Authentication (Register / Login)
- 🔑 Secure password hashing (bcrypt with safety handling)
- 🗄️ PostgreSQL (SQLAlchemy ORM)
- ⚡ Redis (cache-ready)
- 🐳 Docker & Docker Compose
- 🧪 Pytest test scaffolding
- 🔁 GitHub Actions CI (green pipeline)
- 🩺 Health check endpoint
- 📦 Clean, scalable project structure

---

## 🧱 Tech Stack

| Layer        | Technology |
|-------------|------------|
| API         | FastAPI |
| Language    | Python 3.12 |
| Auth        | JWT (python-jose) |
| ORM         | SQLAlchemy |
| Database    | PostgreSQL 15 |
| Cache       | Redis 7 |
| Security    | Passlib + bcrypt |
| CI/CD       | GitHub Actions |
| Containers  | Docker |

---

## 📁 Project Structure

# 🚀 Scalable API Platform

A **production-grade backend system** built with **FastAPI**, designed using **FAANG-level engineering practices** including clean architecture, JWT authentication, CI/CD, Dockerization, and testability.

> Built to demonstrate real-world backend engineering skills for SDE / Backend roles.

---

## ✨ Features

- ✅ FastAPI with Pydantic v2
- 🔐 JWT Authentication (Register / Login)
- 🔑 Secure password hashing (bcrypt with safety handling)
- 🗄️ PostgreSQL (SQLAlchemy ORM)
- ⚡ Redis (cache-ready)
- 🐳 Docker & Docker Compose
- 🧪 Pytest test scaffolding
- 🔁 GitHub Actions CI (green pipeline)
- 🩺 Health check endpoint
- 📦 Clean, scalable project structure

---

## 🧱 Tech Stack

| Layer        | Technology |
|-------------|------------|
| API         | FastAPI |
| Language    | Python 3.12 |
| Auth        | JWT (python-jose) |
| ORM         | SQLAlchemy |
| Database    | PostgreSQL 15 |
| Cache       | Redis 7 |
| Security    | Passlib + bcrypt |
| CI/CD       | GitHub Actions |
| Containers  | Docker |

---

## 📁 Project Structure

scalable-api-platform/
│
├── app/
│ ├── auth/ # Auth routes, schemas, dependencies
│ ├── core/ # Config, database, security
│ ├── models/ # SQLAlchemy models
│ ├── main.py # FastAPI app entry
│
├── tests/ # Pytest tests
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .github
-------------------------------------

## 🔐 Authentication Flow

### Register

/workflows/ci.yml


POST /auth/register
### Login

-----------------------------------------

POST /auth/login

Returns:
```json
{
  "access_token": "<JWT>",
  "token_type": "bearer"
}

--------------------------------------
JWT includes:

sub → user email

iss → scalable-api-platform

exp → configurable expiry
---------------------------------------------
🩺 Health Check

GET /health


Response:

{
  "status": "ok"
}

------------------------
Used by:

CI

Load balancers

Kubernetes readiness (future-ready)

🐳 Run Locally (Docker)
docker compose up --build
-----------------------------------------

Access:

API → http://localhost:8000

Docs → http://localhost:8000/docs

🧪 Run Tests
pytest -v
----------------------------------------------
🔁 CI Pipeline (GitHub Actions)

Every push & PR:

Spins up PostgreSQL + Redis

Installs dependencies

Runs tests

Ensures green builds

✔ Proven by multiple successful CI runs
-------------------------------------------------------
🔒 Security Notes

Passwords hashed using bcrypt

JWT secret injected via environment variables

Password length safely normalized for bcrypt limits

No secrets hardcoded in CI
----------------------------------------------
🎯 Why This Project Matters

This project demonstrates:

Backend system design

Real authentication flows

Production-ready practices

CI/CD discipline

Dockerized development

Perfect for:

Amazon / Microsoft / Google SDE

Backend Engineer roles

System Design discussions
------------------------------------------
🛣️ Roadmap

🔄 Refresh tokens

📊 Metrics & logging

☁️ AWS deployment (ECS / EC2)

🔐 Role-based access control

🧪 Integration tests

👤 Author

Shashi Preetham
Backend / Software Engineer
GitHub: https://github.com/bathinishashipreetham

⭐ If you found this project useful, consider starring it!




