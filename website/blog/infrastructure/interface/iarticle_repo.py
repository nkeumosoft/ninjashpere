import abc
from typing import List
from uuid import UUID

from website.blog.core.interface.iarticle import IArticle


class IArticleRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, uuid: UUID) -> IArticle:
        ...

    @abc.abstractmethod
    def find_by_name(self, name: str) -> IArticle:
        ...

    @abc.abstractmethod
    def find_by_tags(self, tags: UUID) -> IArticle:
        ...

    @abc.abstractmethod
    def update(self, article: IArticle) -> IArticle:
        ...

    @abc.abstractmethod
    def create(self, article: IArticle) -> IArticle:
        ...

    @abc.abstractmethod
    def list(self) -> List[IArticle]:
        ...
