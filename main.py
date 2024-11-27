import uvicorn

from fastapi import FastAPI



from  db.requests import add_child, get_all_children, get_child_by_id

from models import Child

app = FastAPI()

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

    Returns:
        str: Success message.
    """
    add_child(model)
    return "child was added"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)