import abc
from typing import Optional
from uuid import UUID, uuid4


class ITechnology(abc.ABC):
    @abc.abstractmethod
    def name(self) -> str:
        ...

    @abc.abstractmethod
    def logo(self) -> str:
        ...

    @abc.abstractmethod
    def id(self) -> UUID:
        ...

    @classmethod
    def factory(cls, name: str, logo: str, id: Optional[UUID] = None) -> "ITechnology":
        ...
