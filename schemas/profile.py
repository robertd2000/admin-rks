from typing import List
from pydantic import BaseModel, ConfigDict
from enums.profile import GenderEnum, ProfessionEnum, GradeEnum, StatusEnum


class ProfileSchema(BaseModel):
    first_name: str
    last_name: str | None
    age: int | None
    gender: GenderEnum
    profession: ProfessionEnum
    interests: List[str] | None
    contacts: dict | None
    grade: GradeEnum
    status: StatusEnum
    salary: int
    phone: str

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
