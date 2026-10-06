# FastAPI Full-Featured Web Application Course

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Project Overview

Unlike basic API guides, this repository builds a complete, dual-purpose web application from the ground up:

- **JSON REST API:** Secure endpoints structured for programatic access, frontend web frameworks, and mobile clients.
- **Dynamic HTML Frontend:** Server-side rendered interface using **Jinja2** templates and static asset handling for browser interactions.

---

## 🎓 Key Features Covered

### 1. Framework & Core Concepts

- **Environment Setup:** Modern project configuration and fast dependency management using `uv`.
- **Asynchronous Execution:** Understanding `async` / `await` paradigms and route execution performance.
- **Scalable Architecture:** Project modularization using FastAPI’s `APIRouter`.

### 2. Data Management & Validation

- **Data Validation:** Enforcing strict request/response schemas with **Pydantic**.
- **Database Integration:** Setting up **SQLAlchemy ORM** with SQLite for local dev and transitioning to **PostgreSQL**.
- **Schema Migrations:** Versioning database schemas with **Alembic**.

### 3. Security & Advanced Features

- **Authentication:** User registration, password hashing (`passlib`/`bcrypt`), and stateless **JWT** (JSON Web Tokens).
- **File Handling:** Validating and processing media uploads (such as user profile avatars).
- **Background Tasks:** Non-blocking operations like background email dispatching.
- **Testing & Deployment:** Writing test suites with `pytest`, containerization with **Docker**, and production deployment guidelines.

---

## 🛠️ Tech Stack

| Component            | Technology                                     |
| :------------------- | :--------------------------------------------- |
| **Language**         | Python 3.10+                                   |
| **Framework**        | FastAPI                                        |
| **Database**         | SQLite (Development) / PostgreSQL (Production) |
| **ORM & Migrations** | SQLAlchemy, Alembic                            |
| **Data Validation**  | Pydantic v2                                    |
| **Templating**       | Jinja2                                         |
| **Security**         | OAuth2 with Password Bearer, JWT, Passlib      |
| **Package Manager**  | `uv` / `pip`                                   |

---
