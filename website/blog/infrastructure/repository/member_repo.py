from typing import Optional
from uuid import UUID

from website.blog.core.entity.member import MemberEntity
from website.blog.core.interface.imember import IMember
from website.blog.infrastructure.interface.imember_repo import (
    IMemberRepository,
)
from website.blog.models import Member


class MemberRepository(IMemberRepository):
    def __init__(self, member: Member):
        self.member = member

    def find(self, uuid: UUID) -> Optional[IMember]:
        pass

    def find_by_email(self, email: str) -> IMember:
        pass

    def create(self, article: IMember, uuid: UUID) -> IMember:
        pass

    def update(self, member: IMember) -> IMember:
        pass

    def delete(self, uuid: UUID):
        pass

    def factory_member(self):
        return self._factory_member(self.member)

    @staticmethod
    def _factory_member(self, member: Member) -> IMember:
        object_member = MemberEntity.factory(
            uuid=member.uuid,
            name=member.name,
            email=member.email,
            password=member.password,
            is_active=member.is_active,
            date_joined=member.date_joined,
            is_staff=member.is_staff,
        )
        return object_member
