import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from  db.requests import add_child, get_all_children, get_child_by_id, add_raven_test

from models import Child, RavenTest

from psychological_keys import raven_test_key

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return get_all_children()

@app.get("/child/{id}")
def get_child(id: int):
    """
    Get child by id.

    Args:
        id (int): Child id.

    Returns:
        Child: Child object.
    """
    return get_child_by_id(id)

@app.get("/child_test")
def child_test():
    return Child(name="John", surname="Doe", lastname="Smith", age=12, gender="male", groupa="groupa1")


@app.post("/add_child")
def post_add_child(model: Child):
    """
    Add a new child to the database.

    Args:
        model (Child): Child object with the new child's information.
        birthday - d/m/y

    Returns:
        str: Success message.
    """
    add_child(model)
    return "child was added"

@app.post("/add_raven_test")
def post_add_reven_test(model: RavenTest):
    """
    Add a new Raven test result to the database.

    Args:
        model (RavenTest): RavenTest object with the new result's information.

    Returns:
        str: Success message.
    """

    add_raven_test(raven_test_key(model), model.child_id)
    return "result was added"


if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.0.249", port=8000, reload=True)