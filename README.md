#  Employee Management System (FastAPI)

A modern **Employee Management System** built using **Python** and **FastAPI** that provides complete **CRUD (Create, Read, Update, Delete)** functionality for managing employee records. The project follows REST API principles, uses SQLAlchemy ORM for database interactions, and includes automatic API documentation with Swagger UI.

---

## Features

-  Create new employee records
-  Retrieve all employees
-  Retrieve employee by ID
-  Update employee information
-  Delete employee records
-  Input validation using Pydantic
-  Interactive Swagger API Documentation
-  FastAPI high-performance backend
-  Clean project architecture

---

##  Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| FastAPI | Backend Framework |
| SQLite | Database |

---

## 📂 Project Structure

```text
employee-management-system/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       └── employee.py
│
├── requirements.txt
├── README.md
└── employee.db
```

---

##  API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

##  REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/employees/` | Create Employee |
| GET | `/employees/` | Get All Employees |
| GET | `/employees/{id}` | Get Employee by ID |
| PUT | `/employees/{id}` | Update Employee |
| DELETE | `/employees/{id}` | Delete Employee |

---

##  Validation

The application validates:

- Required fields
- Email format
- Data types
- Invalid requests
- Missing resources

---

##  Architecture

```text
Client
   │
   ▼
FastAPI Routes
   │
   ▼
CRUD Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
SQLite Database
```

---

##  Learning Objectives

This project demonstrates:

- Building RESTful APIs with FastAPI
- CRUD Operations
- SQLAlchemy ORM
- Request Validation using Pydantic
- Database Integration
- Clean Project Structure
- API Documentation with Swagger

---

##  Future Improvements

- JWT Authentication
- Role-Based Access Control (RBAC)
- PostgreSQL Support
- Docker Deployment
- Unit Testing
- Pagination
- Search & Filtering
- Sorting
- Logging
- CI/CD Pipeline

---


##  Support

If you found this project useful:

- Star the repository
- Fork the repository
- Contribute to improve the project

---
