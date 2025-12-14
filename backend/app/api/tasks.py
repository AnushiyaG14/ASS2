from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..schemas import TaskCreate, TaskOut
from ..models import Task
from ..crud import create_task, get_all_tasks, get_task_by_id
from ..worker import execute_task
import asyncio

router = APIRouter()

@router.post("/", response_model=TaskOut)
async def create_task_api(
    payload: TaskCreate,
    db: AsyncSession = Depends(get_db)
):
    task = Task(
        name=payload.name,
        type=payload.type,
        execution_time=payload.execution_time,
        status="Pending",
        attempts=0,
        logs=""
    )

    task = await create_task(db, task)

    # background execution (NON-BLOCKING)
    asyncio.create_task(execute_task(task.id))

    return task

@router.get("/", response_model=list[TaskOut])
async def list_tasks_api(db: AsyncSession = Depends(get_db)):
    return await get_all_tasks(db)

@router.get("/{task_id}", response_model=TaskOut)
async def task_detail_api(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
