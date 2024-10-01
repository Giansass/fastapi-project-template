"""aaa"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from ..dependencies import get_token_header

# Parameters
SECRET_KEY = "93a5169cecdc311c4b1557213082083b"  # openssl rand -hex 16
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Router definition
router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# Add OAUTH2 authentication method
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/admin/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    """aaa"""
    return {"token": token}
