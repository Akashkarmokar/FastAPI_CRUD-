from beanie import Document
from typing import List

class Blog(Document):
    title:str
    tags:List[str]
    