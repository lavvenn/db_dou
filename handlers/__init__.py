from fastapi import APIRouter

from handlers.children import router as children_router
from handlers.tests import router as tests_router


router = APIRouter()

router.include_router(children_router)
router.include_router(tests_router)