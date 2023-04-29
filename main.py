from fastapi import FastAPI
import uvicorn
from models import *

app = FastAPI()


def register_function(func: RegisterFn) -> RegisterFnRep:
    print(f'Adding {func.name} to database!')
    func_id = uuid.uuid4()
    return RegisterFnRep(function_id=func_id)


@app.post('/register_function/')
async def create_pie(func: RegisterFn) -> RegisterFnRep:
    return register_function(func)




if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")