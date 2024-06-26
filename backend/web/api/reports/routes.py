from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate

from backend.db import AsyncSession
from backend.models.reports import ReportModel, Report
from backend.web.pagination import Page

router = APIRouter(prefix="/reports")


@router.post("/query", response_model_exclude_none=True)
async def query(sess: AsyncSession, reporter: str | None = None, report_time: str | None = None) -> Page[ReportModel]:
    stmt = Report.build_query(reporter, report_time)
    reports = await paginate(sess, stmt)
    return reports


@router.post("", response_model_exclude_none=True)
async def create(session: AsyncSession, args: ReportModel) -> ReportModel:
    report = await Report.create(session, args.model_dump())
    return report


@router.get("/{id}", response_model_exclude_none=True)
async def get_by_id(session: AsyncSession, id: int) -> ReportModel:
    report = await Report.get_by_id(session, id)
    return report


@router.put("/{id}", response_model_exclude_none=True)
async def update(session: AsyncSession, id: int, args: ReportModel) -> ReportModel:
    report = await Report.update_by_id(session, id, args.model_dump())
    return report


@router.delete("/{id}")
async def delete(session: AsyncSession, id: int) -> None:
    report = await Report.get_by_id(session, id)
    await Report.delete(session, report)
