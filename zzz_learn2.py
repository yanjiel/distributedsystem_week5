from fastapi import FastAPI
from pydantic import BaseModel, constr, validator
from typing import List
import uuid
import uvicorn

app = FastAPI()

class Pie(BaseModel):
    name: constr(max_length=200)
    description: str
    calories: int
    ingredients: List[str]

    @validator('description')
    def ensure_delicious(cls, v):
        if 'delicious' not in v:
            raise ValueError('We only accept delicious pies')
        return v

class RegisterFn(BaseModel):
    name: str
    payload: str
    def __init__(self, name: str, payload: str):
        self.name = name
        self.payload = payload

class RegisterFnRep(BaseModel):
    function_id: uuid.UUID
    def __init__(self, function_id: uuid.UUID):
        self.function_id = function_id


class ExecuteFnReq(BaseModel):
    function_id:uuid.UUID
    payload:str
    def __init__(self, function_id: uuid.UUID, payload: str):
        self.function_id = function_id
        self.payload = payload

class ExecuteFnRep(BaseModel):
    task_id: uuid.UUID
    def __init__(self, task_id: uuid.UUID):
        self.task_id = task_id


class TaskStatusRep(BaseModel):
    task_id:uuid.UUID
    status:str
    def __init__(self, task_id: uuid.UUID, status: str):
        self.task_id = task_id
        self.status = status

def add_pie_to_database(pie: Pie) -> Pie:
    print(f'Adding {pie.name} to database!')
    return pie



@app.post('/pies/')
async def create_pie(pie: Pie):
    return add_pie_to_database(pie)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")