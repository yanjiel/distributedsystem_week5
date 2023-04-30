from fastapi import FastAPI
import uvicorn
from models import *
import json
import redis
import types


app = FastAPI()
r = redis.Redis()
STATUS = {'QUEUED':'QUEUED', 'RUNNING':'RUNNING', 'COMPLETE':'COMPLETE', 'FAILURE':'FAILURE'}

def register(func: RegisterFn) -> RegisterFnRep:
    # print(func.name, func.payload) #"func1", "gASVFgAAAAAAAACMCF9fbWFpbl9flIwFZnVuYzGUk5Qu\n" = codecs.encode(pickle.dumps(func1), "base64").decode()
    # check if the same function with same func.name and func.payload has been registered
    # to-do

    # generate unique uuid for new function to be registered
    func_id = str(uuid.uuid4())
    while func_id in r.keys():
        func_id = str(uuid.uuid4())

    # save into redis database
    r.set(func_id, json.dumps([func.name, func.payload])) #"f1c33bf6-71d2-4d2c-9419-36a21de86d0d", b'{"func1": "gASVFgAAAAAAAACMCF9fbWFpbl9flIwFZnVuYzGUk5Qu\\n"}'

    # print status
    print(f'Adding {func.name} to database! function_id: {func_id}')
    return {"function_id": uuid.UUID(func_id)}




def execute(func_w_param: ExecuteFnReq) -> ExecuteFnRep:
    func_id = str(func_w_param.function_id)
    func_info = json.loads(r.get(func_id))
    print(type(func_info), func_info)

    func_name = func_info[0]
    func_body = deserialize(func_info[1]) #function object
    param = deserialize(func_w_param.payload) #[1,2]

    print(type(func_name), func_name)
    print(type(func_body), func_body)
    print(type(param), param)
    
    # spin up dispatcher to get work done
    if isinstance(func_body, types.FunctionType):
        func_body(*param)
    elif isinstance(func_body, str):
        func_compiled = compile(func_body, func_name, "exec")
        exec(param)
        exec(func_compiled)
    else:
        raise RuntimeError("Deserialized function is of the wrong type.")
    
    # save task future into the db
    # todo

    task_id = str(uuid.uuid4())
    while task_id in r.keys():
        task_id = str(uuid.uuid4())
    return {"task_id": uuid.UUID(task_id)}


def status(task_id: uuid.UUID) -> TaskStatusRep:
    task_info = json.loads(r.get(str(task_id)))
    print(task_info)
    status = STATUS['COMPLETE']
    # future = task_info[0]
    # if future:
    #     status = STATUS['COMPLETE']
    # else:
    #     status = STATUS['RUNINNG']

    return {'task_id': uuid.UUID(task_id), 'status': status}


@app.post('/register_function/')
async def register_function(func: RegisterFn) -> RegisterFnRep:
    return register(func)


@app.post('/execute_fuction/')
async def execute_function(func_w_param: ExecuteFnReq) -> ExecuteFnRep:
    return execute(func_w_param)


@app.post('/status/')
async def get_status(task_id: uuid.UUID) -> TaskStatusRep:
    return status(task_id)



if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
    