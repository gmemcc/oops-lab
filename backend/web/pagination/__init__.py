from typing import Any, Generic, Optional, Sequence, TypeVar

from fastapi import Query
from fastapi_pagination.bases import AbstractPage, AbstractParams, RawParams
from typing_extensions import Self

from backend.models.base import CamelModel


class Params(CamelModel, AbstractParams):
    current: int = Query(1, ge=1)
    pageSize: int = Query(10, ge=1, le=1000)

    def to_raw_params(self) -> RawParams:
        return RawParams(limit=self.pageSize, offset=(self.current - 1) * self.pageSize)


T = TypeVar("T")


class Page(AbstractPage[T], Generic[T]):
    data: Sequence[T]
    success: bool = True
    total: int

    __params_type__ = Params

    @classmethod
    def create(
            cls,
            items: Sequence[T],
            params: AbstractParams,
            *,
            total: Optional[int] = None,
            **kwargs: Any,
    ) -> Self:
        assert isinstance(params, Params)
        assert total is not None

        return cls(
            data=items,
            total=total,
            **kwargs,
        )
