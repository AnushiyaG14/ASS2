from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    name: str
    type: str
    execution_time: int = Field(ge=1, le=60)

class TaskOut(BaseModel):
    id: int
    name: str
    type: str
    execution_time: int
    status: str
    attempts: int
    logs: str

    class Config:
        from_attributes = True
