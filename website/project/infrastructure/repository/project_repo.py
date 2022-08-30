from typing import List
from uuid import UUID

from website.project.core.business.entities import ProjectEntity
from website.project.core.business.interface.iproject import IProject
from website.project.core.business.interface.iproject_repos import IProjectRepository
from website.project.models import Project


class ProjectRepository(IProjectRepository):
    def __init__(self, model: Project):
        self._model = model

    def find(self, uuid: UUID) -> IProject:
        instance = self._model.objects.get(id=uuid)
        return self._fact_project_entity(instance)

    def find_by_name(self, name: str) -> IProject:
        instance = self._model.objects.get(name=name)
        return self._fact_project_entity(instance)

    def create(self, project: IProject) -> None:
        self._model.objects.create(
            name=project.name,
            image=project.image,
            id=project.id,
            description=project.description,
            link=project.url,
            technologies=project.technologies,
        )

    def list(self) -> List[IProject]:
        instances = self._model.objects.all()
        return [self._fact_project_entity(instance) for instance in instances]

    def delete(self, uuid: UUID) -> None:
        self._model.objects.get(id=uuid).delete()

    @staticmethod
    def _fact_project_entity(instance: Project) -> IProject:
        return ProjectEntity.factory(
            instance.name,
            instance.description,
            instance.image,
            instance.technologies,
            instance.link,
            instance.id,
        )
