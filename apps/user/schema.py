from pydantic import root_validator, validators
from tortoise.contrib.pydantic import pydantic_model_creator

from .models import UserModel


# Generate custom pydantic model class based on database Model
BasePydanticUserModel = pydantic_model_creator(UserModel)


class UserModelSerializer(BasePydanticUserModel):
    # validate single field
    # pre means before parsing, by default its after parsing
    @validators("username", pre=True)
    def validate_username(cls, value):
        return value

    # validate all fields
    @root_validator(pre=True)
    def validate_all_fields(cls, values):
        return values
