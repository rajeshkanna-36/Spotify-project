from enum import Enum
from pydantic import BaseModel


class AdminRole(str, Enum):
    MANAGER = "manager"
    DEVELOPER = "developer"
    CONTENT_MANAGER = "content_manager"


class AdminSignup(BaseModel):
    admin_id: int
    role: AdminRole
    password: str


class AdminLogin(BaseModel):
    admin_id: int
    password: str