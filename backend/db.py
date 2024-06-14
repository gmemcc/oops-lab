import logging
from typing import Annotated, AsyncIterator

from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from settings import settings

logger = logging.getLogger(__name__)

async_engine = create_async_engine(
    settings.db_url,
    pool_pre_ping=True,
    echo=settings.echo_sql,
    pool_size=settings.db_pool_size,
    max_overflow=settings.db_max_overflow,
)
async_sessionmaker_local = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    future=True,
)


async def get_async_session() -> AsyncIterator[AsyncSession]:
    session = async_sessionmaker_local()
    try:
        logger.debug("Creating async session")
        yield session
        logger.debug("Committing async session")
        await session.commit()
    except SQLAlchemyError:
        logger.debug("Rolling back async session")
        await session.rollback()
        raise
    finally:
        logger.debug("Closing async session")
        await session.close()


AsyncSession = Annotated[AsyncIterator[AsyncSession], Depends(get_async_session)]
