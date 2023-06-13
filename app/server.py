from fastapi import FastAPI
from core.config import config
from .routes import initRoutes
from core.db.models import allModels
from core.db.connection import init_db



def create_app():
    app = FastAPI(
        title="Protfolio",
        description="Nice to see you again",
        version="1.0.0",
        docs_url= None  if config.stage == 'production' else "/docs",
        redoc_url= None if config.stage == 'production' else "/rdoc",
    )
    initRoutes(app_= app)
    
    return app




root_app = create_app()

@root_app.on_event('startup')
async def DatabaseConnection():
    await init_db(allModels)