from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    # created_at:
    # updated_at:


class Poll(BaseModel):
    title: str
    type: str
    is_voting_allowed: bool
    is_adding_choices_allowed: bool
