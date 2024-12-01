import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from  db.requests import add_child, all_children, child_by_id, add_raven_test, add_emotion_test, remove_child_by_id

from models import Child, RavenTest, EmotionTest

from psychological_keys import raven_test_key, emotions_test_key

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["children🧒"])
def get_all_children():
    return all_children()

@app.get("/children/{id}", tags=["children🧒"])
def get_child(id: int):
    """
    Get child by id.

    Args:
        id (int): Child id.

    Returns:
        Child: Child object.
    """
    return child_by_id(id)


@app.post("/children/add", tags=["children🧒"])
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

@app.delete("/children/delete/{id}", tags=["children🧒"])
def delete_child(id: int):
    remove_child_by_id(id)
    return "child was deleted"


@app.post("/tests/raven/add", tags=["tests📝"])
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

@app.post("/tests/emotions/add", tags=["tests📝"])
def post_add_emotional_test(model: EmotionTest):
    """
    Add a new Emotional test result to the database.

    Args:
        model (EmotionTest): EmotionalTest object with the new result's information.

    Returns:
        str: Success message.
    """

    add_emotion_test(emotions_test_key(model), model.child_id)
    return "result was added"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)