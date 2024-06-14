from __future__ import annotations

from typing import Self
from datetime import datetime
from sqlalchemy import String, select, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from backend.db import AsyncSession
from backend.models.base import CamelModel, Base


class Report(Base):
    __tablename__ = "reports"
    id: Mapped[int] = mapped_column("id", autoincrement=True, primary_key=True, comment="id of the report")
    reporter: Mapped[str] = mapped_column("reporter", String, nullable=False, comment="reporter")
    report_time: Mapped[datetime] = mapped_column("report_time", DateTime, nullable=False, comment="report time")
    work_content: Mapped[str] = mapped_column("work_content", String, nullable=False, comment="work content")
    concerned_incs: Mapped[str] = mapped_column("concerned_incs", String, nullable=False, comment="concerned incs")

    @classmethod
    def build_query(cls, reporter: str | None, work_content: str | None, report_time: str | None):
        stmt = select(cls)
        where = None
        if reporter:
            where = cls.reporter.like(f"%{reporter}%")
        if work_content:
            where |= cls.work_content.like(f"%{work_content}%")
        if report_time:
            report_time_start = datetime.strptime(report_time, "%Y-%m-%d")
            report_time_end = report_time_start.replace(hour=23, minute=59, second=59)
            where |= cls.report_time.between(report_time_start, report_time_end)

        if where is not None:
            stmt = stmt.where(where)
        stmt = stmt.order_by(cls.id.asc())
        return stmt

    @classmethod
    async def create(cls, session: AsyncSession, args: dict[str, any]) -> Self:
        report = cls(**args)
        session.add(report)
        await session.flush()
        return report

    @classmethod
    async def delete(cls, session: AsyncSession, report: Report) -> None:
        await session.delete(report)
        await session.flush()

    @classmethod
    async def delete_by_id(cls, session: AsyncSession, report_id: int) -> None:
        report = await cls.get_by_id(session, report_id)
        await cls.delete(session, report)

    @classmethod
    async def get_by_id(cls, session: AsyncSession, report_id: int) -> Report:
        return (await session.execute(select(cls).where(cls.id == report_id))).scalar_one()

    @classmethod
    async def read_all(cls, session: AsyncSession) -> list[Report]:
        return (await session.execute(select(cls))).scalars().all()

    @classmethod
    async def update(cls, session: AsyncSession, report: Report, args: dict[str, any]) -> Report:
        for key, value in args.items():
            setattr(report, key, value)
        await session.flush()
        return report

    @classmethod
    async def update_by_id(cls, session: AsyncSession, report_id: int, args: dict[str, any]) -> Report:
        report = await cls.get_by_id(session, report_id)
        return await cls.update(session, report, args)

    @classmethod
    async def delete_by_ids(cls, session: AsyncSession, report_ids: list[int]) -> None:
        for report_id in report_ids:
            await cls.delete_by_id(session, report_id)

    @classmethod
    async def get_by_ids(cls, session: AsyncSession, report_ids: list[int]) -> list[Report]:
        return (await session.execute(select(cls).where(cls.id.in_(report_ids)))).scalars().all()


class ReportModel(CamelModel):
    id: int | None
    reporter: str | None
    report_time: datetime | None
    work_content: str | None
    concerned_incs: str | None
