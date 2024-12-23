from pydantic import BaseModel, ConfigDict

from schemas.profile import ProfileSchema


class EmployeeSchema(BaseModel):
    username: str
    email: str
    profile: ProfileSchema | None

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
