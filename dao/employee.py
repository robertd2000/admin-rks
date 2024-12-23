from sqlalchemy.ext.asyncio import AsyncSession

from dao.base import BaseDAO
from models.employee import Employee
from models.profile import Profile


class EmployeeDAO(BaseDAO):
    model = Employee

    @classmethod
    async def add_employee(cls, session: AsyncSession, data: dict) -> Employee:
        employee = cls.model(username=data['username'], email=data['email'])
        session.add(employee)
        await session.flush()

        profile = Profile(
            user_id=employee.id,
            first_name=employee['first_name'],
            last_name=employee.get('last_name'),
            age=employee.get('age'),
            gender=employee['gender'],
            profession=employee.get('profession'),
            salary=employee.get('salary'),
            phone=employee.get('phone'),
            contacts=employee.get('contacts'),
            interests=employee.get('interests'),
            status=employee.get('status'),
            grade=employee.get('grade'),
        )

        session.add(profile)
        await session.commit()

        return employee

