import uvicorn
from core.config import config


def main():
    uvicorn.run(
        app='app.server:root_app',
        reload= True if config.stage != 'production' else False
    )

if __name__ == "__main__":
    main()