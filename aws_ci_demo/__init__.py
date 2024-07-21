import uuid

from fastapi import FastAPI
import threading
import time
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "hello world"}


@app.get("/{param}")
def read_param(param: str):
    return {"received_param": param}


def print_hello_world():
    while True:
        time.sleep(5)
        print(f"hello world: " + str(uuid.uuid4().hex))


if __name__ == "__main__":
    thread = threading.Thread(target=print_hello_world, daemon=True)
    thread.start()
    uvicorn.run(app, port=8080)
