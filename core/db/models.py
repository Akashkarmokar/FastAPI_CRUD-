from beanie import Document
from typing import List
from auth.model import User as UserModel
from blog.model import Blog as BlogModel



allModels: List[Document] = [
    UserModel,
    BlogModel
]
