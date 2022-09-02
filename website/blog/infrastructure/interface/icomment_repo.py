import abc
from uuid import UUID

from website.blog.core.interface.icomment import IComment


class ICommentRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, uuid: UUID) -> IComment:
        ...

    @abc.abstractmethod
    def find_by_name(self, name: str) -> IComment:
        ...

    @abc.abstractmethod
    def find_by_tags(self, tags: UUID) -> IComment:
        ...

    @abc.abstractmethod
    def update(self, article: IComment) -> IComment:
        ...

    @abc.abstractmethod
    def create(self, article: IComment, uuid: UUID) -> IComment:
        ...

    @abc.abstractmethod
    def get_author(self, uuid: UUID) -> UUID:
        ...

    @abc.abstractmethod
    def get_post(self, uuid: UUID) -> UUID:
        ...
