import abc
from typing import Dict, List
from uuid import UUID

from project.core.business.interface.itechnology import ITechnology


class ITechnologyUseCase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, uuid: UUID) -> ITechnology:
        ...

    @abc.abstractmethod
    def find_by_name(self, name: str) -> ITechnology:
        ...

    @abc.abstractmethod
    def create(self, data: Dict) -> None:
        ...

    @abc.abstractmethod
    def list(self) -> List[ITechnology]:
        ...
