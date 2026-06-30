# CodeSync

A real-time collaborative coding platform built with **FastAPI, React, PostgreSQL, SQLAlchemy, WebSockets, JWT, and Docker**. CodeSync enables multiple users to collaborate on code in shared rooms with secure authentication and persistent document storage.

> 🚧 **Project Status:** Ongoing

---

## Features

### Implemented

- FastAPI backend
- PostgreSQL integration
- SQLAlchemy ORM
- JWT Authentication
- User Registration & Login APIs
- Room Creation API
- Dockerized backend setup
- Adminer database interface

### 🚧 Ongoing

- Real-time collaborative editing using WebSockets
- Shared coding rooms
- Persistent document storage
- React frontend
- Version history
- Role-based room access
- Docker Compose deployment
- Monaco Code Editor integration

---

## Tech Stack

**Backend**
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- WebSockets

**Frontend**
- React *(Ongoing)*

**DevOps**
- Docker
- Docker Compose

**Tools**
- Adminer
- Git

---

## Project Structure

```text
codesync/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── websocket/
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/              # Ongoing
│
├── docker-compose.yaml
└── README.md
```

---

## Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd codesync
```

### Start services

```bash
docker compose up --build
```

### Run backend locally

```bash
cd backend

python -m venv .venv

.venv\Scripts\activate      # Windows

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

Adminer

```
http://localhost:8080
```

---



---


