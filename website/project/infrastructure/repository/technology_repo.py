from typing import List
from uuid import UUID

from project.core.business.entities import TechnologyEntity
from project.core.business.interface.itechnology import ITechnology
from project.core.business.interface.itechnology_repos import ITechnologyRepository
from project.models import Technology


class TechnologyRepository(ITechnologyRepository):
    def __init__(self, model: Technology):
        self._model = model

    def find(self, uuid: UUID) -> ITechnology:
        instance = self._model.objects.get(id=uuid)
        return self._fact_techno_entity(instance)

    def find_by_name(self, name: str) -> ITechnology:
        instance = self._model.objects.get(name=name)
        return self._fact_techno_entity(instance)

    def create(self, tech: ITechnology) -> None:
        self._model.objects.create(name=tech.name, logo=tech.logo, id=tech.id)

    def list(self) -> List[ITechnology]:
        instances = self._model.objects.all()
        return [self._fact_techno_entity(instance) for instance in instances]

    def delete(self, uuid: UUID) -> None:
        self._model.objects.get(id=uuid).delete()

    @staticmethod
    def _fact_techno_entity(instance: Technology) -> ITechnology:
        return TechnologyEntity.factory(instance.name, instance.logo, instance.id)
