from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uuid


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

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

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# def register_function(regfun: RegisterFn) -> RegisterFnRep:
#     pass
# def execute_function(exefun: ExecuteFnReq) -> ExecuteFnRep:
#     pass
# def get_status(task_id: uuid.UUID) -> TaskStatusRep:
#     pass




@app.put("/register_function{}")

@app.get("/status/{task_id}")
def get_status(task_id: uuid.UUID):
    status = ""
    TaskStatusRep(task_id=task_id, status=status)
    return TaskStatusRep





import dill
import codecs

def serialize(obj) -> str:
    return codecs.encode(dill.dumps(obj), "base64").decode()

def deserialize(obj: str):
    return dill.loads(codecs.decode(obj.encode(),"base64"))





# this will be invoked by uvicorn main:app --host 127.0.0.1 --port 6379 --reload (this should be abandoned)
# main.py
import uvicorn

async def read_body(receive):
    """
    Read and return the entire body from an incoming ASGI message.
    """
    body = b''
    more_body = True

    while more_body:
        message = await receive()
        body += message.get('body', b'')
        more_body = message.get('more_body', False)

    return body


async def app(scope, receive, send):
    assert scope['type'] == 'http'

    #body = f'Received {scope["method"]} request to {scope["path"]}'
    body = await read_body(receive)
     
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            (b'content-type', b'text/plain'),
            (b'content-length', str(len(body)).encode())
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': body,
    })


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
# uvicorn zzz_learnfastapi:app --reload
# go to http://127.0.0.1:8000 to see the return message in the function that's appended @app.get("/")
# ctrl+c to shutdown