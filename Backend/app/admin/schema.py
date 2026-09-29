from enum import Enum
from pydantic import BaseModel


class AdminRole(str, Enum):
    MANAGER = "manager"
    DEVELOPER = "developer"
    CONTENT_MANAGER = "content_manager"


class admin_signup(BaseModel):
    admin_id: int
    role: AdminRole
    password: str


class admin_login(BaseModel):
    admin_id: int
    password: str