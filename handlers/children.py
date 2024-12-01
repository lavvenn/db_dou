from fastapi import APIRouter

from db.requests import add_child, all_children, child_by_id, remove_child_by_id
from models import Child

router = APIRouter(
    prefix="/children",
    tags=["children🧒"]
)



@router.get("/")
def get_all_children():
    return all_children()

@router.get("/{id}")
def get_child(id: int):
    """
    Get child by id.

    Args:
        id (int): Child id.

    Returns:
        Child: Child object.
    """
    return child_by_id(id)


@router.post("/add")
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

@router.delete("/delete/{id}")
def delete_child(id: int):   
    return remove_child_by_id(id)


