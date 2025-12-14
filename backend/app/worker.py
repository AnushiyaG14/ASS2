import asyncio
import random
from .database import AsyncSessionLocal
from .crud import get_task_by_id, update_task

async def execute_task(task_id: int):
    async with AsyncSessionLocal() as db:
        task = await get_task_by_id(db, task_id)
        if not task:
            return

        while task.attempts < 3:
            task.status = "Running"
            task.logs += "Task started\n"
            await update_task(db, task)

            await asyncio.sleep(task.execution_time)

            if random.random() < 0.7:
                task.status = "Completed"
                task.logs += "Task completed successfully\n"
                await update_task(db, task)
                return
            else:
                task.attempts += 1
                task.logs += f"Attempt {task.attempts} failed\n"
                await update_task(db, task)

        task.status = "Failed"
        task.logs += "Task permanently failed after 3 attempts\n"
        await update_task(db, task)
