import abc
from typing import List
from uuid import UUID

from blog.core.business.interface.imember import IMember


class IMemberUseCase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_member(self, name: str, email: str, password: str) -> None:
        ...

    @abc.abstractmethod
    def list_members(self) -> None:
        ...

    @abc.abstractmethod
    def update_member(self, member_id: UUID, name: str, email: str) -> None:
        ...

    @abc.abstractmethod
    def delete_member(self, member_id: UUID) -> None:
        ...

    @abc.abstractmethod
    def get_member(self, member_id: UUID) -> IMember:
        ...

    @abc.abstractmethod
    def get_members_by_name(self, name: str) -> List[IMember]:
        ...
