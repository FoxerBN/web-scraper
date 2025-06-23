from pydantic import BaseModel
from typing import Optional

class House(BaseModel):
    title: str
    price: str
    link: str
    location: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    views: Optional[str] = None
