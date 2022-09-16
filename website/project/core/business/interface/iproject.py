import abc
from typing import List, Optional
from uuid import UUID, uuid4

from project.core.business.interface.itechnology import ITechnology


class IProject(abc.ABC):
    @abc.abstractmethod
    def id(self) -> UUID:
        ...

    @abc.abstractmethod
    def name(self) -> str:
        ...

    @abc.abstractmethod
    def description(self) -> str:
        ...

    @abc.abstractmethod
    def image(self) -> str:
        ...

    @abc.abstractmethod
    def technologies(self) -> List[ITechnology]:
        ...

    @abc.abstractmethod
    def url(self) -> str:
        ...

    @classmethod
    def factory(
        cls,
        name: str,
        description: str,
        image: str,
        technologies: List[ITechnology],
        url: str,
        id: Optional[UUID] = None,
    ) -> "IProject":
        ...
