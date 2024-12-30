from typing import List

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from dao.employee import EmployeeDAO
from db.decorators import connection
from schemas.employee import EmployeeCreate, EmployeeSchema
from schemas.profile import ProfileEditSchema


@connection
async def edit_employee(data: ProfileEditSchema, employee_id: int, session: AsyncSession) -> int:
    employee_dict = data.model_dump()

    try:
        updated_employee = await EmployeeDAO.update_employee(session, employee_id=employee_id, data=employee_dict)
        return updated_employee.id
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=''.join(e.detail))


@connection
async def get_all_employees(session: AsyncSession) -> List[EmployeeSchema]:
    return await EmployeeDAO.get_all(session)


@connection
async def get_employee_by_id(employee_id: int, session: AsyncSession) -> EmployeeSchema:
    return await EmployeeDAO.get_by_id(session=session, data_id=employee_id)


@connection
async def create_employee(data: EmployeeCreate, session: AsyncSession) -> int:
    employee_dict = data.model_dump()

    try:
        employee = await EmployeeDAO.add_employee(session=session, data=employee_dict)

        return employee.id
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=''.join(e.detail))


@connection
async def delete_employee(employee_id: int, session: AsyncSession):
    result = await EmployeeDAO.delete(query_id=employee_id, session=session)

    return result
