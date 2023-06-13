from fastapi import FastAPI,status, Response, APIRouter
from . import schemas

blogRouter = APIRouter()


@blogRouter.post('/',status_code=status.HTTP_201_CREATED)
async def createBlog(requestedBlogData: schemas.SingleBlog, response: Response):
    print(requestedBlogData.tags)
    if len(requestedBlogData.tags) == 0 :
        response.status_code = status.HTTP_400_BAD_REQUEST
        return "Blog is not created"
    return 'Blog is creating'