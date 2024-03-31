from pydantic import BaseModel


class correct_user(BaseModel):
    image: str | None = None
    username: str
    countries: str
    hobby: list[str]
