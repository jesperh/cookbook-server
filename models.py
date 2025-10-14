from pydantic import BaseModel
from typing import List, Optional

class Recipe(BaseModel):
    name: str
    description: Optional[str] = None
    ingredients: List[str]