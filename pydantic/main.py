from pydantic import BaseModel
from datetime import date
from bson import ObjectId
from enum import Enum

class PermissionLevel(Enum):
    COMMON = 1
    STAFF = 2
    ADMIN = 3
    SUPERUSER = 4


class User(BaseModel):
    name: str
    #store: ObjectId
    created_at: date
    permission_level: PermissionLevel


user = User(
    name="Victor", created_at=date.today(), permission_level=PermissionLevel.SUPERUSER
)
print(user, type(user))
print(user.name)