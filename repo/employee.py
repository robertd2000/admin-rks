from sqlalchemy.ext.asyncio import AsyncSession

from dao.employee import EmployeeDAO
from db.decorators import connection


@connection
async def add_employee(user_data: dict, session: AsyncSession) -> int:
    new_employee = EmployeeDAO.add_employee(session, **user_data)
    print(f"Добавлен новый пользователь с ID: {new_employee.id}")
    return new_employee.id

