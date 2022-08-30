from dataclasses import dataclass, field
from typing import List, Optional
from uuid import UUID, uuid4

from website.project.core.business.interface.iproject import IProject
from website.project.core.business.interface.itechnology import ITechnology


@dataclass
class TechnologyEntity(ITechnology):
    _name: str
    _logo: str
    _id: UUID = field(default=uuid4())

    @property
    def name(self):
        return self._name

    @property
    def logo(self):
        return self._logo

    @property
    def id(self):
        return self._id

    @classmethod
    def factory(cls, name: str, logo: str, id: Optional[UUID] = None) -> ITechnology:
        id = id or uuid4()
        obj = cls(name, logo, id)
        return obj


@dataclass
class ProjectEntity(IProject):
    _name: str
    _description: str
    _image: str
    _technologies: List[ITechnology]
    _url: str
    _id: UUID = field(default=uuid4())

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def image(self):
        return self._image

    @property
    def technologies(self):
        return self._technologies

    @property
    def url(self):
        return self._url

    @classmethod
    def factory(
        cls,
        name: str,
        description: str,
        image_path: str,
        technologies: List[ITechnology],
        url: str,
        id: Optional[UUID] = None,
    ) -> IProject:
        id = id or uuid4()
        obj = cls(name, description, image_path, technologies, url, id)
        return obj
