from sqlalchemy.ext.asyncio import AsyncSession

from dao.base import BaseDAO
from models.employee import Employee
from models.profile import Profile


class EmployeeDAO(BaseDAO):
    model = Employee

    @classmethod
    async def add_employee(cls, session: AsyncSession, data: dict) -> Employee:
        profile = Profile(
            first_name=data['first_name'],
            last_name=data.get('last_name'),
            age=data.get('age'),
            gender=data['gender'],
            profession=data.get('profession'),
            salary=data.get('salary'),
            phone=data.get('phone'),
            contacts=data.get('contacts'),
            interests=data.get('interests'),
            status=data.get('status'),
            grade=data.get('grade'),
        )

        session.add(profile)
        await session.flush()

        employee = cls.model(username=data['username'], email=data['email'], profile_id=profile.id)
        session.add(employee)

        await session.commit()

        return employee
