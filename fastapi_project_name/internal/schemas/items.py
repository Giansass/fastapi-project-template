"""Users schema"""
from pydantic import BaseModel, Field


class ItemInfo(BaseModel):
    """UserName data model"""

    item: str = Field(title="Item id", max_length=50)
    name: str = Field(title="Item name", max_length=50)
    description: str = Field(title="Item description", max_length=50)
    price: float | None = Field(default=None, title="Item price", examples=[2, 34.2, "47"])

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item": "Pasta",
                    "name": "Pasta Integrale",
                    "description": "Pasta integrale 500gr",
                    "price": 3.15,
                }
            ]
        }
    }
