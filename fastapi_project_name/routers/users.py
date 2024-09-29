"""An example of router used to retrieve username"""

from fastapi import APIRouter

# Router definition
router = APIRouter()


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    """Return the username"""
    return {"username": username}
