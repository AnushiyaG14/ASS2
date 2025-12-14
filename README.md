## Task Runner App

### Run
docker compose up --build

### Backend
- FastAPI async
- Background task execution
- Retry logic (max 3)
- PostgreSQL only

### Frontend
- Nuxt 3 SSR
- Polling every 3s
- Pinia store

### Key Guarantees
- No blocking calls
- No SQLite
- SSR used correctly
- Docker reliable
