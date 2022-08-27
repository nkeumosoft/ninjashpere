from dataclasses import dataclass, field
from typing import List, Optional
from uuid import UUID, uuid4


@dataclass
class Technology:
    _name: str
    _logo: str
    _id: Optional[UUID] = None

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
    def factory(cls, name: str, logo: str, id: Optional[UUID] = None):
        id = id or uuid4()
        obj = cls(_id=id, _name=name, _logo=logo)
        return obj


@dataclass
class Project:
    _name: str
    _description: str
    _image: str
    _technologies: List[Technology]
    _url: str
    _id: Optional[UUID] = None

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
        technologies: List[Technology],
        url: str,
        id: Optional[UUID] = None,
    ):
        id = id or uuid4()
        obj = cls(
            _id=id,
            _name=name,
            _description=description,
            _image=image_path,
            _technologies=technologies,
            _url=url,
        )
        return obj
