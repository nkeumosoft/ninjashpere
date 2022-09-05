from dataclasses import dataclass
from typing import Dict, List
from uuid import UUID

from project.core.business.entities import ProjectEntity
from project.core.business.interface.iproject import IProject
from project.core.business.interface.iproject_repos import IProjectRepository
from project.core.business.interface.iproject_uc import IProjectUseCase


@dataclass
class ProjectManagement(IProjectUseCase):
    _project_repository: IProjectRepository

    def find(self, uuid: UUID) -> IProject:
        return self._project_repository.find(uuid)

    def find_by_name(self, name: str) -> IProject:
        return self._project_repository.find_by_name(name)

    def create(self, data: Dict) -> None:
        project = ProjectEntity.factory(
            name=data["name"],
            description=data["description"],
            image_path=data["image"],
            technologies=data["technologies"],
            url=data["url"],
        )
        self._project_repository.create(project)

    def list(self) -> List[IProject]:
        return self._project_repository.list()
