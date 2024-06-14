from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
# noinspection PyPackageRequirements
from humps import camelize
from pydantic import BaseModel

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    __abstract__ = True
    metadata = MetaData(naming_convention=convention)

    def __repr__(self) -> str:
        columns = ", ".join(
            [f"{k}={repr(v)}" for k, v in self.__dict__.items() if not k.startswith("_")]
        )
        return f"<{self.__class__.__name__}({columns})>"


class CamelModel(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_alias = True
        populate_by_name = True
        from_attributes = True
