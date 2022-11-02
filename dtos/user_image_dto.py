from pydantic import BaseModel


class UserImageBaseDto(BaseModel):
    image: str


class UserImageDto(UserImageBaseDto):
    id: int
