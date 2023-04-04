from pydantic import BaseModel


class GetUsersSchema(BaseModel):
    name: str
    email: str
