from sqlalchemy.exc import SQLAlchemyError
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

    @classmethod
    async def update_employee(cls, session: AsyncSession, employee_id: int, data: dict) -> Employee:
        employee = await cls.get_by_id(session=session, data_id=employee_id)

        try:
            employee.profile.first_name = data.get('first_name')
            employee.profile.last_name = data.get('last_name')
            employee.profile.age = data.get('age')
            employee.profile.gender = data['gender']
            employee.profile.profession = data.get('profession')
            employee.profile.salary = data.get('salary')
            employee.profile.phone = data.get('phone')
            employee.profile.contacts = data.get('contacts')
            employee.profile.interests = data.get('interests')
            employee.profile.status = data.get('status')
            employee.profile.grade = data.get('grade')

            await session.flush()

            return employee
        except SQLAlchemyError as e:
            print(f"Error occurred: {e}")
            raise
