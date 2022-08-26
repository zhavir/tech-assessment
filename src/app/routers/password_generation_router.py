from starlette import status

from app.routers import router
from app.routers.models.requests import GeneratePasswordRequest
from app.routers.models.responses import GeneratedPasswordResponse
from app.services.password_generator_service import PasswordGeneratorService


@router.post(
    path='/generate/',
    status_code=status.HTTP_200_OK,
    response_model=GeneratedPasswordResponse,
)
async def generate_password(request: GeneratePasswordRequest) -> GeneratedPasswordResponse:
    password = PasswordGeneratorService().generate_password(
        password_length=request.password_length,
        has_numbers=request.has_numbers,
        has_lowercase_chars=request.has_lowercase_chars,
        has_uppercase_chars=request.has_uppercase_chars,
        has_special_chars=request.has_special_chars,
    )
    return GeneratedPasswordResponse(password=password)
