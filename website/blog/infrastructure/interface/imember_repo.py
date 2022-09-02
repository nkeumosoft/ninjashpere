import abc
from typing import Optional
from uuid import UUID

from website.blog.core.interface.imember import IMember
from website.blog.models import Member


class IMemberRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, uuid: UUID) -> Optional[IMember]:
        ...

    @abc.abstractmethod
    def find_by_email(self, email: str) -> IMember:
        ...

    @abc.abstractmethod
    def create(self, article: IMember, uuid: UUID) -> IMember:
        ...

    @abc.abstractmethod
    def update(self, member: IMember) -> IMember:
        ...

    @abc.abstractmethod
    def delete(self, uuid: UUID):
        ...

    @staticmethod
    def _factory_member(self, member: Member) -> IMember:
        ...
