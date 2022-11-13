from pydantic import BaseModel, validator
from datetime import date, timedelta
from bson import ObjectId
from enum import Enum
from typing import Optional

class PermissionLevel(Enum):
    COMMON = 1
    STAFF = 2
    ADMIN = 3
    SUPERUSER = 4


class User(BaseModel):
    name: str
    #store: ObjectId
    created_at: date
    permission_level: Optional[PermissionLevel]

    @validator("name")
    def validate_name(cls, name):
        if " " in name:
            raise ValueError("Name must be a single name not a full name!")
        name

    @validator("permission_level")
    def validate_permission_level_from_created_at(cls, permission_level, values):
        if permission_level:
            limit_date = date.today() + timedelta(days=365)
            if (limit_date.year - values["created_at"].year) <= 1 and permission_level in (PermissionLevel.SUPERUSER, PermissionLevel.ADMIN):
                raise ValueError("For the desired permission level the user must have been created for more than one year.")
            permission_level
        permission_level

valid_user = User(
    name="Victor", created_at=date(1993, 11, 8), permission_level=PermissionLevel.SUPERUSER
)

invalid_user = User(
    name="Victor", created_at=date(2022, 11, 13), permission_level=PermissionLevel.SUPERUSER
)

valid_user2 = User(
    name="Santos", created_at=date.today()
)

