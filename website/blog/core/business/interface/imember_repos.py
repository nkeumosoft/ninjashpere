import abc
from typing import List
from uuid import UUID

from blog.core.business.interface.imember import IMember


class IMemberRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, member_id: UUID) -> IMember:
        ...

    @abc.abstractmethod
    def find_by_name(self, name: str) -> List[IMember]:
        ...

    @abc.abstractmethod
    def create(self, member: IMember) -> None:
        ...

    @abc.abstractmethod
    def list(self) -> List[IMember]:
        ...

    @abc.abstractmethod
    def delete(self, uuid: UUID) -> None:
        ...

    @abc.abstractmethod
    def update(self, id_member: UUID, member_data: IMember) -> None:
        ...
