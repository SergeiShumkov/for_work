from dataclasses import Field
from xml.dom import ValidationErr
from pydantic import BaseModel, validator, Field



class Post(BaseModel):
    name: str = Field(min_length=11)
    value: str

    @validator("name")
    def check_LOC(cls, v):
        if "LOC" not in v:
            raise ValueError("name is not include 'LOC'")
        else:
            return v