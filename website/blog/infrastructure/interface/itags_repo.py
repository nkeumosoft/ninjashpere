import abc
from uuid import UUID

from website.blog.core.interface.itags import ITags


class ITagsRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, uuid: UUID) -> ITags:
        ...

    @abc.abstractmethod
    def find_by_name(self, name: str) -> ITags:
        ...

    @abc.abstractmethod
    def find_by_tags(self, tags: UUID) -> ITags:
        ...

    @abc.abstractmethod
    def create(self, article: ITags) -> ITags:
        ...
