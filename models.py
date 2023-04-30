from pydantic import BaseModel
import uuid
import pickle
import codecs

class RegisterFn(BaseModel):
    name: str
    payload: str
    # def __init__(self, name: str, payload: str):
    #     self.name = name
    #     self.payload = payload

class RegisterFnRep(BaseModel):
    function_id: uuid.UUID
    # def __init__(self, function_id: uuid.UUID):
    #     self.function_id = function_id


class ExecuteFnReq(BaseModel):
    function_id:uuid.UUID
    payload:str
    # def __init__(self, function_id: uuid.UUID, payload: str):
    #     self.function_id = function_id
    #     self.payload = payload

class ExecuteFnRep(BaseModel):
    task_id: uuid.UUID
    # def __init__(self, task_id: uuid.UUID):
    #     self.task_id = task_id


class TaskStatusRep(BaseModel):
    task_id:uuid.UUID
    status:str
    # def __init__(self, task_id: uuid.UUID, status: str):
    #     self.task_id = task_id
    #     self.status = status


def serialize(obj) -> str:
    return codecs.encode(pickle.dumps(obj), "base64").decode()

def deserialize(obj: str):
    return pickle.loads(codecs.decode(obj.encode(),"base64"))

