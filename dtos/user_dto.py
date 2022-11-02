from pydantic import BaseModel


class UserBaseDto(BaseModel):
    name: str


class UserDto(UserBaseDto):
    id: int
