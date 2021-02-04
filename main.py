import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from views import home

api = fastapi.FastAPI()


def configure_routing():
    api.mount('/assets', StaticFiles(directory='assets'), name='assets')
    api.include_router(home.router)


def configure():
    configure_routing()


if __name__ == '__main__':
    configure()
    uvicorn.run(api)
else:
    configure()
