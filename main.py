import uvicorn

from fastapi import FastAPI



from  db import add_child, print_children

from models import Child

app = FastAPI()

@app.get("/")
def root():
    return print_children()

@app.get("/child_test")
def child_test():
    return Child(name="John", surname="Doe", lastname="Smith", age=12, gender="male", groupa="groupa1")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)