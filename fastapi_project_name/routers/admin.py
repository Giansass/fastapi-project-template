"""aaa"""

from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

from ..internal.utils.utils import SecretKeyGenerator

# # Parameters
# SECRET_KEY = "93a5169cecdc311c4b1557213082083b"  # openssl rand -hex 16
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30


secret_key = SecretKeyGenerator()


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

# Router definition
router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


def fake_hash_password(password: str):
    """aaa"""
    return "fakehashed" + password


# Add OAUTH2 authentication method
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# class User(BaseModel):
#     """aaa"""
#
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None
#
#
# class UserInDB(User):
#     """aaa"""
#
#     hashed_password: str
#
#
# def get_user(db, username: str):
#     """aaa"""
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#
#
# def fake_decode_token(token):
#     """aaa"""
#     user = get_user(fake_users_db, token)
#     return user
#
#
# @router.get("/admin/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     """aaa"""
#     return {"token": token}
