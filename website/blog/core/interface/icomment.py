import abc
from datetime import datetime
from typing import Optional
from uuid import UUID


class IComment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def likes(self) -> int:
        ...

    @abc.abstractmethod
    def id(self):
        ...

    def author(self):
        ...

    @abc.abstractmethod
    def date_comment(self) -> str:
        ...

    @abc.abstractmethod
    def content(self) -> str:
        ...

    @classmethod
    def factory(
        cls,
        uuid: UUID,
        post: UUID,
        date_comment: datetime,
        content: str,
        likes: int,
        author: Optional[UUID],
    ) -> "IComment":
        ...
