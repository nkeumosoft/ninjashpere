from typing import List
from uuid import UUID

from django.contrib.auth.models import User

from blog.core.business.entities import MemberEntity
from blog.core.business.interface.imember import IMember
from blog.core.business.interface.imember_repos import IMemberRepository
from blog.models import Member


class MemberRepository(IMemberRepository):
    def __init__(self, model: Member):
        self._model = model

    def find(self, member_id: UUID) -> IMember:
        instance = self._model.objects.get(id=member_id)
        return self._factory_member_entity(instance)

    def find_by_name(self, name: str) -> List[IMember]:
        instances = self._model.objects.filter(user__last_name__contains=name)
        return [self._factory_member_entity(instance) for instance in instances]

    def create(self, member: IMember) -> None:
        user = User.objects.create_user(
            id=member.uuid,
            username=member.email,
            last_name=member.name,
            password=member.password,
        )
        self._model.objects.create(id=member.uuid, user=user)

    def list(self) -> List[IMember]:
        instances = self._model.objects.all()
        return [self._factory_member_entity(instance) for instance in instances]

    def delete(self, uuid: UUID) -> None:
        User.objects.get(id=uuid).delete()

    def update(self, id_member: UUID, member_data: IMember) -> None:
        ...

    @staticmethod
    def _factory_member_entity(instance: Member) -> IMember:
        return MemberEntity.factory(
            instance.user.last_name,
            instance.user.username,
            instance.user.password,
            instance.id,
        )
