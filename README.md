# 🚀 Task Runner Application (Assessment 2)

A full-stack web application that allows users to create background tasks, define execution time, and track their execution status in real time.

This project was built as part of **Developer Assessment – Task 2**, with a strong focus on **async execution, clean architecture, Docker reliability, and production best practices**.

---

## 🧩 Tech Stack

### Backend
- FastAPI (async)
- SQLAlchemy (Async ORM)
- Alembic (migrations)
- PostgreSQL
- Python 3.12

### Frontend
- Nuxt 3
- Server-Side Rendering (SSR)
- Pinia (state management)
- TypeScript

### Infrastructure
- Docker
- Docker Compose

---

## 🏗️ Architecture Overview

```text
Browser (localhost:3000)
        ↓
Nuxt 3 Frontend (SSR + Pinia)
        ↓ HTTP (JSON APIs)
FastAPI Backend (localhost:8000)
        ↓
PostgreSQL Database


Why this architecture?

Frontend and backend are fully decoupled

Backend supports async, non-blocking execution

Database persistence across restarts

Easy local setup using Docker Compose

🔄 Task Lifecycle

Each task follows a strict lifecycle:

Pending → Running → Completed / Failed


Invalid state transitions are prevented.

🔁 Retry Logic

Each task starts with attempts = 0

Tasks may randomly fail (simulated)

On failure:

Attempts increase

Task retries automatically

Maximum retries: 3

After 3 failures → task is marked Failed

⏱️ Async Execution (Key Requirement)

Tasks execute outside the API request

API responds immediately

Execution uses:

await asyncio.sleep(execution_time)


❌ No blocking calls (time.sleep) are used

🎨 Frontend Features

Server-side rendered (SSR) initial load

Task creation form

Live task dashboard

Automatic status updates using polling

Task detail view with execution logs

User-friendly toast notifications

🗄️ Database

PostgreSQL only (no SQLite)

Stores:

Task name

Task type

Execution time

Status

Attempts

Execution logs

Managed using Alembic migrations

🐳 Running the Application
Prerequisites

Docker

Docker Compose

Start the app
docker compose up --build

🌍 Access URLs
Service	URL
Frontend	http://localhost:3000

Backend API	http://localhost:8000/tasks/

API Docs	http://localhost:8000/docs
🧪 How to Verify Everything Works

Open frontend → http://localhost:3000

Create a task with execution time (e.g., 3 seconds)

Task appears immediately

Status updates automatically:

Pending → Running → Completed


Refresh page → task still exists (DB persistence)

Create multiple tasks → observe retries on failures

📁 Project Structure
ASS2/
├── backend/
│   ├── app/
│   ├── alembic/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── stores/
│   ├── nuxt.config.ts
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
├── README.md
└── .gitignore

🔐 Security & Best Practices

.env files ignored via .gitignore

No secrets committed

Containers run in isolation

PostgreSQL used consistently across environments

Versions pinned for predictable builds

✅ Assessment Requirements Checklist
Requirement	Status
FastAPI async backend	✅
Background task execution	✅
Retry logic (max 3)	✅
User-defined execution time	✅
Nuxt 3 SSR	✅
Pinia state management	✅
PostgreSQL only	✅
Docker Compose setup	✅
User-friendly notifications	✅

📌 Notes

This project focuses on correct async handling, clean separation of concerns, and real-world deployment practices, addressing all feedback from the previous assessment.


---

## ✅ Now: SHOULD YOU PUSH?

👉 **YES — after this formatting fix, push immediately.**

### Commands to run:

```bash
git add README.md
git commit -m "Improve README with professional documentation"
git push
