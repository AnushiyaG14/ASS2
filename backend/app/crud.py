from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import Task

async def create_task(db: AsyncSession, task: Task) -> Task:
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_all_tasks(db: AsyncSession):
    result = await db.execute(select(Task).order_by(Task.id.desc()))
    return result.scalars().all()

async def get_task_by_id(db: AsyncSession, task_id: int) -> Task | None:
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalar_one_or_none()

async def update_task(db: AsyncSession, task: Task):
    await db.commit()
    await db.refresh(task)
    return task
