from fastapi import FastAPI
from pydantic import BaseModel, constr, validator
from typing import List
import uvicorn


class Pie(BaseModel):
    name: constr(max_length=200)
    description: str
    calories: int
    ingredients: List[str]

app = FastAPI()


def add_pie_to_database(pie: Pie) -> Pie:
    print(f'Adding {pie.name} to database!')
    return pie


@app.post('/pies/')
async def create_pie(pie: Pie):
    return add_pie_to_database(pie)

if __name__ == "__main__":
    uvicorn.run("testmain:app", host="127.0.0.1", port=5000, log_level="info")