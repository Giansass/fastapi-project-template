"""Routers to manage users"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status

from ..dependencies import get_token_header
from ..internal.schemas.users import UserInfo

# Router definition
router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# List granted users
granted_usernames = {"andrea.giansanti": {"name": "Andrea", "surname": "Giansanti", "age": 34}}


@router.get("/", status_code=status.HTTP_200_OK)
async def read_items():
    """Get all users"""
    return granted_usernames


@router.get("/read_usernames/", status_code=status.HTTP_200_OK)
async def read_user(username: Annotated[str | None, Query(max_length=50)] = None):
    """Return the required user"""
    if username not in granted_usernames:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return (
        {
            "name": granted_usernames[username]["name"],
            "surname": granted_usernames[username]["surname"],
            "age": granted_usernames[username]["age"],
        }
        if username is not None
        else granted_usernames
    )


@router.post("/add_username", status_code=status.HTTP_201_CREATED)
async def add_username(userinfo: UserInfo):
    """Add the required user"""
    granted_usernames[userinfo.user] = {
        "name": userinfo.name,
        "surname": userinfo.surname,
        "age": userinfo.age,
    }
    return {"message": f"Username {userinfo.user} added"}


@router.put("/update_username", status_code=status.HTTP_202_ACCEPTED)
async def update_name(userinfo: UserInfo):
    """Update the required user"""
    if userinfo.user not in granted_usernames:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    granted_usernames[userinfo.user] = {
        "name": userinfo.name,
        "surname": userinfo.surname,
        "age": userinfo.age,
    }
    return {"message": f"Username {userinfo.user} updated"}


@router.delete("/delete_username/{username}", status_code=status.HTTP_202_ACCEPTED)
async def delete(username: str):
    """Delete the required user"""
    if username not in granted_usernames:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    del granted_usernames[username]
    return {"message": f"Username {username} deleted"}
