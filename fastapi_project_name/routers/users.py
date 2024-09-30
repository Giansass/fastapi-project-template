"""An example of router used to retrieve username"""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from ..dependencies import get_token_header


class UserInfo(BaseModel):
    """UserName data model"""

    user: str
    name: str
    surname: str
    age: int | None = None


# Router definition
router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# List granted users
granted_usernames = {"andrea.giansanti": {"name": "Andrea", "surname": "Giansanti", "age": 34}}


@router.get("/")
async def read_items():
    """Get all users"""
    return granted_usernames


@router.get("/{username}")
async def read_user(username: str):
    """Return the required user"""
    if username not in granted_usernames:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "name": granted_usernames[username]["name"],
        "surname": granted_usernames[username]["surname"],
        "age": granted_usernames[username]["age"],
    }


@router.post("/add_username")
async def add_username(userinfo: UserInfo):
    """Add the required user"""
    # global granted_usernames
    granted_usernames[userinfo.user] = {
        "name": userinfo.name,
        "surname": userinfo.surname,
        "age": userinfo.age,
    }
    return granted_usernames


@router.put("/{username}")
async def update_name(username: str):
    """Update the required user"""
    return username


@router.delete("/{username}")
async def delete(username: str):
    """Delete the required user"""
    return username
