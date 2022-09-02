import abc
from datetime import datetime
from uuid import UUID


class IArticle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def id(self):
        ...

    @abc.abstractmethod
    def title(self):
        ...

    def content(self):
        ...

    @abc.abstractmethod
    def picture(self):
        ...

    @abc.abstractmethod
    def author(self):
        ...

    @abc.abstractmethod
    def publish(self):
        ...

    @abc.abstractmethod
    def publish_date(self) -> str:
        ...

    @abc.abstractmethod
    def last_edit(self):
        ...

    @abc.abstractmethod
    def likes(self):
        ...

    @classmethod
    def factory(
        cls,
        uuid: UUID,
        title: str,
        content: str,
        picture: str,
        author: UUID,
        publish_date: datetime,
        last_edit: datetime,
        likes: int,
        publish: bool,
    ) -> "IArticle":
        pass

    def get_picture(self, uuid: UUID):
        ...
