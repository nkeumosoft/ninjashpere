import abc
from typing import Dict, List
from uuid import UUID

from project.core.business.interface.iproject import IProject


class IProjectUseCase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, uuid: UUID) -> IProject:
        ...

    @abc.abstractmethod
    def find_by_name(self, name: str) -> IProject:
        ...

    @abc.abstractmethod
    def create(self, data: Dict) -> None:
        ...

    @abc.abstractmethod
    def list(self) -> List[IProject]:
        ...
