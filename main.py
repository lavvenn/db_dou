import uvicorn

from fastapi import FastAPI



from  db import add_child, print_children, get_child_by_id

from models import Child

app = FastAPI()

@app.get("/")
def root():
    return print_children()

@app.get("/child/{id}")
def get_child(id: int):
    return get_child_by_id(id)

@app.get("/child_test")
def child_test():
    return Child(name="John", surname="Doe", lastname="Smith", age=12, gender="male", groupa="groupa1")


@app.post("/add_child")
def post_add_child(model: Child):
    add_child(model)
    return "child was added"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)