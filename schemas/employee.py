from typing import List

from pydantic import BaseModel, ConfigDict

from enums.profile import GenderEnum, ProfessionEnum, GradeEnum, StatusEnum
from schemas.profile import ProfileSchema


class EmployeeSchema(BaseModel):
    id: int
    username: str
    email: str
    profile: ProfileSchema | None

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)


class EmployeeCreate(BaseModel):
    username: str
    email: str
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
