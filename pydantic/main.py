from pydantic import BaseModel, validator
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

    @validator("created_at")
    def validate_date(cls, created_at):
        if created_at.year > date.today().year:
            raise ValueError("Year must be lass than or equal to current year!")
        created_at


valid_user = User(
    name="Victor", created_at=date.today(), permission_level=PermissionLevel.SUPERUSER
)

invalid_user = User(
    name="Victor", created_at=date(2045, 11, 13), permission_level=PermissionLevel.SUPERUSER
)


