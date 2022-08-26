import argparse

import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.openapi.utils import get_openapi


APP_VERSION = 1.0
SERVICE_NAME = 'Password Generator'
SERVICE_DESCRIPTION = 'The password generator service'

app = FastAPI(title=SERVICE_NAME, description=SERVICE_DESCRIPTION)

# Main routers for API versioning
router_api = APIRouter()
router_api_v1 = APIRouter()
# Registration of routes


# Finalizing setup of router with FastAPI app
router_api.include_router(router_api_v1, prefix="/v1")
app.include_router(router_api, prefix="/api")


# OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=SERVICE_NAME,
        version=f"{APP_VERSION}",
        description=SERVICE_DESCRIPTION,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=9001)
    parser.add_argument('--host', type=str, default="0.0.0.0")
    parser.add_argument('--reload', action='store_true', default=True)

    args = parser.parse_args()
    host = args.host
    port = args.port
    reload = args.reload

    uvicorn.run('main:app', host=host, port=port, reload=reload)
