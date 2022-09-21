from dataclasses import dataclass
from typing import List
from uuid import UUID

from blog.core.business.entities import MemberEntity
from blog.core.business.interface.imember import IMember
from blog.core.business.interface.imember_repos import IMemberRepository
from blog.core.business.interface.imember_usecase import IMemberUseCase


@dataclass
class MemberManagement(IMemberUseCase):
    _member_repository: IMemberRepository

    def create_member(self, name: str, email: str, password: str) -> None:
        member = MemberEntity.factory(name, email, password)
        self._member_repository.create(member)

    def list_members(self) -> List[IMember]:
        return self._member_repository.list()

    def update_member(self, member_id: UUID, name: str, email: str) -> None:
        ...

    def delete_member(self, member_id: UUID) -> None:
        self._member_repository.delete(member_id)

    def get_member(self, member_id: UUID) -> IMember:
        return self._member_repository.find(member_id)

    def get_members_by_name(self, name: str) -> List[IMember]:
        return self._member_repository.find_by_name(name)
