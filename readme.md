need to understand redis server
    https://redis.io/docs/getting-started/installation/install-redis-on-windows/
    Redis is only available in Linux, so need to install Ubuntu on WSL. Enter Ubuntu by going powershell and bash (given Ubuntu is default on WSL)
    Inside bash, need to use python3, sudo apt install uvicorn, sudo apt install redis
    Then can run redis-server on Ubuntu (give all redis-server ports are not in use, other wise redis-cli shutdonw)
    Then can run uvicorn main:app --reload (--host 127.0.0.1 --port 5000)

need to understand uvicorn main:app --reload
    https://fastapi.tiangolo.com/deployment/manually/
    https://www.uvicorn.org/
    It's how a FASTAPI based server can be run, by utilizing uvicorn




learn fastapi
    https://fastapi.tiangolo.com/
    fastapi concurrency
    https://fastapi.tiangolo.com/async/#in-a-hurry

need to first research about Redis db it's message broker capacity, like Redis.sub("Task")
need to understand the payload


use fastapi w redis
    https://ubaydah.hashnode.dev/building-a-blog-service-with-fastapi-and-redis-om
    https://progressivecoder.com/fastapi-event-driven-architecture-example-using-redis/
    https://testdriven.io/courses/fastapi-celery/getting-started/