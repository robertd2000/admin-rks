from typing import List

from fastapi import APIRouter, status

from service.employee import get_all_employees, create_employee, delete_employee
from schemas.employee import EmployeeSchema, EmployeeCreate

router = APIRouter(prefix='/employees', tags=['employees'])


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_employee_route(data: EmployeeCreate):
    employee_id = await create_employee(data)

    return {'status': 'success', 'message': f'ID {employee_id} успешно добавлен.'}


@router.get('/', response_model=List[EmployeeSchema], status_code=status.HTTP_200_OK)
async def get_all_employees_route():
    return await get_all_employees()


@router.delete('/{employee_id}')
async def delete_employee_route(employee_id: int):
    return await delete_employee(employee_id=employee_id)
