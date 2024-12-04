from fastapi import APIRouter

from db.requests import add_emotion_test, add_raven_test, add_relation_test, raven_test_by_child_id, relation_test_by_child_id, emotion_test_by_child_id, all_raven_tests, all_emotion_tests, all_relation_tests
from models import EmotionTest, RavenTest, RelationTest
from psychological_keys import emotions_test_key, raven_test_key, relation_test_key

router = APIRouter(
    prefix="/tests",
    tags=["tests📝"]
)

@router.get("/raven")
def get_all_raven_tests():
    return all_raven_tests()


@router.get("/emotions")
def get_all_emotion_tests():
    return all_emotion_tests()


@router.get("/relation")
def get_all_relation_tests():
    return all_relation_tests()


@router.get("/raven/child/{id}")
def get_raven_test_by_child_id(child_id: int):
    return raven_test_by_child_id(child_id)

@router.get("/emotions/child/{id}")
def get_emotion_test_by_child_id(child_id: int):
    return emotion_test_by_child_id(child_id)

@router.get("/relation/child/{id}")
def get_relation_test_by_child_id(child_id: int):
    return relation_test_by_child_id(child_id)

@router.post("/raven/add")
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

@router.post("/emotions/add")
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

@router.post("/relation/add")
def post_add_relation_test(model: RelationTest):
    """
    Add a new Relation test result to the database.

    Args:
        model (RelationTest): RelationTest object with the new result's information.

    Returns:
        str: Success message.
    """

    add_relation_test(relation_test_key(model), model.child_id)
    return "result was added"