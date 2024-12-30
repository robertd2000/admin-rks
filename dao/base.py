from typing import List, Any, Dict

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, session: AsyncSession, **values):
        new_instance = cls.model(**values)
        session.add(new_instance)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instance

    @classmethod
    async def get_all(cls, session: AsyncSession):
        query = select(cls.model)
        result = await session.execute(query)
        records = result.scalars().all()

        return records

    @classmethod
    async def get_by_id(cls, session: AsyncSession, data_id: int):
        try:
            return await session.get(cls.model, data_id)
        except SQLAlchemyError as e:
            print(f"Error occurred: {e}")
            raise

    @classmethod
    async def delete(cls, session: AsyncSession, query_id: int):
        try:
            query = select(cls.model).filter_by(id=query_id)
            result = await session.execute(query)
            employee = result.scalar_one_or_none()

            if not employee:
                return {
                    'message': f"ID {query_id} не найден.",
                    'status': 'error'
                }

            await session.delete(employee)
            await session.commit()

            return {
                'message': f"ID {query_id} успешно удален.",
                'status': 'success'
            }

        except SQLAlchemyError as e:
            await session.rollback()
            return {
                'message': f"Произошла ошибка при удалении: {str(e)}",
                'status': 'error'
            }
