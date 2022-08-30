import abc
from typing import List
from uuid import UUID

from website.project.core.business.interface.itechnology import ITechnology


class ITechnologyRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, uuid: UUID) -> ITechnology:
        ...

    @abc.abstractmethod
    def find_by_name(self, name: str) -> ITechnology:
        ...

    @abc.abstractmethod
    def create(self, tech: ITechnology) -> None:
        ...

    @abc.abstractmethod
    def list(self) -> List[ITechnology]:
        ...

    @abc.abstractmethod
    def delete(self, uuid: UUID) -> None:
        ...
