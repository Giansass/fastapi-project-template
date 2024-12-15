"""Main module"""
from fastapi import FastAPI

from .routers import admin, items

# from .dependencies import get_query_token, get_token_header
# from .internal import admin


app = FastAPI()
app.include_router(items.router)
app.include_router(admin.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    """root msg"""
    return {"message": "Hello Bigger Applications!"}
