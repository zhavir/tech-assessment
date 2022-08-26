from pydantic import BaseModel


class GeneratedPasswordResponse(BaseModel):
    password: str
