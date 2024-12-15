"""Users schema"""
from pydantic import BaseModel, Field


class UserInfo(BaseModel):
    """UserName data model"""

    user: str = Field(title="User id", max_length=50)
    name: str = Field(title="User name", max_length=50)
    surname: str = Field(title="User surname", max_length=50)
    age: int | None = Field(default=None, title="User age", max_length=3, examples=[2, 34, "47"])

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "user": "andrea.giansanti",
                    "name": "Andrea",
                    "surname": "Giansanti",
                    "age": 34,
                }
            ]
        }
    }
