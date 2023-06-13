from fastapi import FastAPI
from blog.main import blogRouter
from auth.main import authRouter

def initRoutes(app_:FastAPI)->None:
    app_.include_router(authRouter,prefix="/auth",tags=["auth"])
    app_.include_router(blogRouter,prefix="/blog",tags=["blog"])

