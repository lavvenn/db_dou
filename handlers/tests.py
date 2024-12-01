from fastapi import APIRouter

from db.requests import add_emotion_test, add_raven_test
from models import EmotionTest, RavenTest
from psychological_keys import emotions_test_key, raven_test_key

router = APIRouter(
    prefix="/tests",
    tags=["tests📝"]
)

@router.post("/raven/add", tags=["tests📝"])
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

@router.post("/emotions/add", tags=["tests📝"])
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