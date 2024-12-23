from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base
from models.profile import Profile


class Employee(Base):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)

    profile_id: Mapped[int | None] = mapped_column(ForeignKey('profiles.id'))
    profile = relationship("Profile", back_populates="employee", uselist=False, lazy="joined")
