from pydantic import BaseModel
from typing import List,Optional

class SingleBlog(BaseModel):
    title: str
    tags: Optional[List[str]]