from pydantic import BaseModel, validator

from src.enums.value_enums import Values, NameErrors


class Settings(BaseModel):
    name: str  
    # Если поле необязательное , то писать 'name: str = None', 'name: str = ""', 'name: str = 0'
    value: str
    # value: Values

    @validator("name")
    def check_that_LOC_presented_in_name(cls, name):
        if 'LOC.' in name:
            return name
        else:
            raise ValueError(NameErrors.WRONG_Name.value)
    
