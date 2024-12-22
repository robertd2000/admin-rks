import enum


class GenderEnum(str, enum.Enum):
    MALE = "мужчина"
    FEMALE = "женщина"


class ProfessionEnum(str, enum.Enum):
    DEVELOPER = "разработчик"
    DESIGNER = "дизайнер"
    MANAGER = "менеджер"
    TEACHER = "учитель"
    DOCTOR = "врач"
    ENGINEER = "инженер"
    MARKETER = "маркетолог"
    WRITER = "писатель"
    ARTIST = "художник"
    LAWYER = "юрист"
    SCIENTIST = "ученый"
    NURSE = "медсестра"
    UNEMPLOYED = "безработный"


class GradeEnum(str, enum.Enum):
    JUNIOR = "JUNIOR"
    MIDDLE = "MIDDLE"
    SENIOR = "SENIOR"

class StatusEnum(str, enum.Enum):
    ACTIVE = "Активен"
    BANNED = "Заблокирован"