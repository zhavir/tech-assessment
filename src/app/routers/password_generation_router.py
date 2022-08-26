from starlette import status

from app.routers import router
from app.routers.models.requests import GeneratePasswordRequest
from app.routers.models.responses import GeneratedPasswordResponse


@router.post(
    path='/generate/',
    status_code=status.HTTP_200_OK,
    response_model=GeneratedPasswordResponse,
)
async def generate_password(request: GeneratePasswordRequest) -> GeneratedPasswordResponse:
    return GeneratedPasswordResponse(password="something")
