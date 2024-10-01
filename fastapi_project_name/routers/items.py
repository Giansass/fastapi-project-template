"""Routers to manage users"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status

from ..dependencies import get_token_header
from ..internal.schemas.items import ItemInfo

# Router definition
router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# List granted users
items = {"Pasta": {"name": "Pasta", "description": "Pasta integrale 500gr", "price": 3.15}}


@router.get("/", status_code=status.HTTP_200_OK)
async def read_items():
    """Get all items"""
    return items


@router.get("/read_items/", status_code=status.HTTP_200_OK)
async def read_item(item: Annotated[str | None, Query(max_length=50)] = None):
    """Return the required user"""
    if item not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    return {
        "name": items[item]["name"],
        "surname": items[item]["description"],
        "age": items[item]["price"],
    }


@router.post("/add_item", status_code=status.HTTP_201_CREATED)
async def add_item(iteminfo: ItemInfo):
    """Add the required user"""
    items[iteminfo.item] = {
        "name": iteminfo.name,
        "description": iteminfo.description,
        "price": iteminfo.price,
    }
    return {"message": f"Item {iteminfo.item} added"}


@router.put("/update_item", status_code=status.HTTP_202_ACCEPTED)
async def update_item(iteminfo: ItemInfo):
    """Update the required user"""
    if iteminfo.item not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    items[iteminfo.item] = {
        "name": iteminfo.name,
        "description": iteminfo.description,
        "price": iteminfo.price,
    }
    return {"message": f"Item {iteminfo.item} updated"}


@router.delete("/delete_item/{item}", status_code=status.HTTP_202_ACCEPTED)
async def delete(item: str):
    """Delete the required user"""
    if item not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    del items[item]
    return {"message": f"Item {item} deleted"}
