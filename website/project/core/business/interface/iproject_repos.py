import abc
from typing import List
from uuid import UUID

from website.project.core.business.interface.iproject import IProject


class IProjectRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, uuid: UUID) -> IProject:
        ...

    @abc.abstractmethod
    def find_by_name(self, name: str) -> IProject:
        ...

    @abc.abstractmethod
    def create(self, project: IProject) -> None:
        ...

    @abc.abstractmethod
    def list(self) -> List[IProject]:
        ...

    @abc.abstractmethod
    def delete(self, uuid: UUID) -> None:
        ...
