🚀 Task Runner Application (Assessment-2)

Project: Background Task Runner
Stack: Nuxt 3 + FastAPI + PostgreSQL
Author: Anushiya
Purpose: Developer Assessment – Async Task Execution System

👋 Overview

This application allows users to create background tasks, define how long they should run, and track their execution status in real time.

Tasks are executed asynchronously, do not block API responses, and follow a strict lifecycle with retry logic.

This project demonstrates production-grade full-stack development using modern best practices.

🏗️ Architecture (Big Picture)

Frontend and backend are fully decoupled and communicate only via JSON APIs.

Browser (Port 3000)
        ↓
Nuxt 3 Frontend (SSR + Pinia)
        ↓ HTTP (JSON)
FastAPI Backend (Port 8000)
        ↓
PostgreSQL Database (Port 5432)

Why this architecture?

Frontend and backend can scale independently

Clean separation of concerns

Backend can later support mobile apps or other clients without changes

🐍 Backend – FastAPI

Located in /backend

Key Responsibilities

Accept task creation requests

Execute tasks asynchronously

Manage task lifecycle & retries

Persist task state in PostgreSQL

🔁 Task Lifecycle

Every task strictly follows this flow:

Pending → Running → Completed OR Failed


Invalid transitions are prevented by design.

🔄 Retry Logic

Each task starts with attempts = 0

On failure:

Attempts increment

Task retries automatically

Maximum retries: 3

After 3 failures → task marked as Failed

⏱️ Async Execution (Core Requirement)

Tasks run outside the API request

API responds immediately

Execution uses:

await asyncio.sleep(execution_time)


🚫 time.sleep() is never used

🗄️ Database (PostgreSQL)

Each task stores:

Name

Type (notification / processing)

Execution time (seconds)

Status

Attempts

Execution logs

PostgreSQL is used in ALL environments
(No SQLite anywhere)

🔐 CORS Configuration

The backend explicitly allows requests from:

http://localhost:3000


This enables safe browser communication while preventing unauthorized access.

🎨 Frontend – Nuxt 3

Located in /frontend

Key Responsibilities

Task creation UI

Dashboard showing task status

Task detail & logs view

Live status updates

⚡ Server-Side Rendering (SSR)

Initial page load uses Nuxt SSR.

Benefits:

Faster first render

Better SEO

No empty pages on load

📦 State Management – Pinia

Pinia is used to:

Store task list

Fetch tasks from backend

Share state across components cleanly

This avoids:

Prop drilling

Duplicate API calls

🔄 Live Updates (Polling)

Frontend polls backend every few seconds

Status updates automatically without page refresh

Polling runs only in browser, not during SSR

🔔 User Feedback

Success and failure messages shown via toast notifications

Errors are not silently hidden

🐳 Docker & Deployment

The entire system runs using Docker Compose.

Services

frontend → Nuxt 3 SSR

backend → FastAPI

db → PostgreSQL

▶️ Run the Application

From project root:

docker compose up --build

🌍 Access URLs
Service	URL
Frontend	http://localhost:3000

Backend API	http://localhost:8000/tasks/

API Docs	http://localhost:8000/docs
📁 Project Structure
ASS2/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   ├── worker.py
│   │   └── api/
│   │       └── tasks.py
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
└── README.md

🧪 How to Verify Backend Is Working

Create a task from UI

Task appears immediately

Status updates automatically:

Pending → Running → Completed


Refresh page → task still exists

View logs on task detail page

✅ Confirms:

Async execution

Database persistence

Correct lifecycle handling

🧠 ORM & Database Layer

ORM: SQLAlchemy (Async)

DB Driver (runtime): asyncpg

Migrations: Alembic (sync engine)

Why?

Async DB operations for performance

Stable schema management

Production-ready design

✅ Assessment Requirements Checklist
Requirement	Status
FastAPI backend	✅
Async execution	✅
No blocking calls	✅
User-defined execution time	✅
Retry logic (max 3)	✅
Task lifecycle enforced	✅
Nuxt SSR frontend	✅
Pinia state management	✅
PostgreSQL only	✅
Docker Compose	✅
🎯 Final Notes

This project:

Fixes all issues from Assessment-1

Uses each technology for its intended purpose

Is production-ready and reviewer-friendly
