from fastapi import APIRouter

router: APIRouter = APIRouter()

from .password_generator_router import generate_password
