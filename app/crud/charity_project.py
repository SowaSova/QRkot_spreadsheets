from typing import Optional

from sqlalchemy import asc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):
    @staticmethod
    async def get_project_id_by_name(
        charity_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        charity_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_name
            )
        )
        charity_id = charity_id.scalars().first()
        return charity_id

    @staticmethod
    async def get_projects_by_completion_rate(
        session: AsyncSession,
    ) -> Optional[CharityProject]:
        closed_projects = await session.execute(
            select(CharityProject)
            .where(CharityProject.fully_invested == 1)
            .order_by(
                asc(
                    func.datediff(
                        CharityProject.close_date, CharityProject.create_date
                    )
                )
            )
        )
        closed_projects = closed_projects.scalars().all()
        return closed_projects


charity_project_crud = CRUDCharityProject(CharityProject)
