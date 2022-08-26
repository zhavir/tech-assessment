from fastapi import APIRouter

router: APIRouter = APIRouter()

from .password_generation_router import generate_password
