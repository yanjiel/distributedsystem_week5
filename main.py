from fastapi import FastAPI
import uvicorn
from models import *
import json
import redis

app = FastAPI()
r = redis.Redis()

def register(func: RegisterFn) -> RegisterFnRep:
    # print(func.name, func.payload) #"func1", "gASVFgAAAAAAAACMCF9fbWFpbl9flIwFZnVuYzGUk5Qu\n" = codecs.encode(pickle.dumps(func1), "base64").decode()
    # check if the same function with same func.name and func.payload has been registered
    # to-do

    # generate unique uuid for new function to be registered
    func_id = str(uuid.uuid4())
    while func_id in r.keys():
        func_id = str(uuid.uuid4())

    # save into redis database
    r.set(func_id, json.dumps({func.name:func.payload})) #"f1c33bf6-71d2-4d2c-9419-36a21de86d0d", b'{"func1": "gASVFgAAAAAAAACMCF9fbWFpbl9flIwFZnVuYzGUk5Qu\\n"}'

    # print status
    print(f'Adding {func.name} to database! function_id: {func_id}')
    return {"function_id": uuid.UUID(func_id)}



@app.post('/register_function/')
async def register_function(func: RegisterFn) -> RegisterFnRep:
    return register(func)

# code_compiled = compile("print(x+y)","func1","exec")
# param="x=1;y=2"
# exec(param)
# exec(code_compiled)

def execute(func_w_param: ExecuteFnReq) -> ExecuteFnRep:
    func_id = str(func_w_param.function_id)
    param = str(func_w_param.payload)
    func_info = r.get(func_id)
    
    func_compiled = compile(deserialize(func_info.payload), func_info.name, "exec")
    exec(param) ######################################
    exec(func_compiled) ##############################

    task_id = str(uuid.uuid4())
    while task_id in r.keys():
        task_id = str(uuid.uuid4())
    return {"task_id": uuid.UUID(task_id)}


@app.get('/execute_fuction/')
async def execute_function(func_w_param: ExecuteFnReq) -> ExecuteFnRep:
    return execute(func_w_param)


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")