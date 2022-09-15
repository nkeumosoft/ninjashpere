from dataclasses import dataclass
from typing import Dict, List
from uuid import UUID

from project.core.business.entities import TechnologyEntity
from project.core.business.interface.itechnology import ITechnology
from project.core.business.interface.itechnology_repos import ITechnologyRepository
from project.core.business.interface.itechnology_uc import ITechnologyUseCase


@dataclass
class TechnologyManagement(ITechnologyUseCase):
    _technology_repository: ITechnologyRepository

    def find(self, uuid: UUID) -> ITechnology:
        return self._technology_repository.find(uuid)

    def find_by_name(self, name: str) -> ITechnology:
        return self._technology_repository.find_by_name(name)

    def create(self, data: Dict) -> None:
        technology = TechnologyEntity.factory(
            name=data["name"],
            logo=data["logo"],
        )
        self._technology_repository.create(technology)

    def list(self) -> List[ITechnology]:
        return self._technology_repository.list()
