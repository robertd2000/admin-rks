from typing import List

from sqlalchemy import text, ARRAY, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base
from enums.profile import GenderEnum, ProfessionEnum, StatusEnum, GradeEnum


class Profile(Base):
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    age: Mapped[int | None]
    gender: Mapped[GenderEnum]
    profession: Mapped[ProfessionEnum] = mapped_column(
        default=ProfessionEnum.DEVELOPER,
        server_default=text("'UNEMPLOYED'")
    )
    salary: Mapped[int]
    phone: Mapped[str] = mapped_column(String, unique=True)
    interests: Mapped[List[str] | None] = mapped_column(ARRAY(String))
    contacts: Mapped[dict | None] = mapped_column(JSON)
    status: Mapped[StatusEnum] = mapped_column(
        default=StatusEnum.ACTIVE,
        server_default=text("'ACTIVE'")
    )
    grade: Mapped[GradeEnum] = mapped_column(
        default=GradeEnum.JUNIOR,
        server_default=text("'JUNIOR'")
    )
    user: Mapped["User"] = relationship("User", back_populates="profile", uselist=False)
