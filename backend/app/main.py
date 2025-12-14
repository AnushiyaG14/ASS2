from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import tasks

app = FastAPI()

# ✅ ADD CORS MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ SINGLE PREFIX ONLY
app.include_router(tasks.router, prefix="/tasks")
