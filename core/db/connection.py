import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document
from typing import List

async def init_db(Models: List[Document]):
    if len(Models):
        client = AsyncIOMotorClient("mongodb://localhost:27017")
        await init_beanie(database=client.db_name, document_models= Models)
    # else :
    #     # Make error call we stop our server to start connection
    