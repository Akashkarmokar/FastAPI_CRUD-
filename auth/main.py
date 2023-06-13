from fastapi import APIRouter
from pydantic import BaseModel
from .model import User

authRouter = APIRouter()


@authRouter.get('/')
async def getAllUsers():
    users = await User.find_all().to_list()
    return users

@authRouter.post('/signin')
async def signIn():
    return "SignIn Router"



class SignUpDTO(BaseModel):
    email: str
    password: str


@authRouter.post('/signup')
async def signUp(signUpDTO: SignUpDTO):
    user = User(email=signUpDTO.email, password= signUpDTO.password)
    createdUser = await User.create(user)
    return createdUser