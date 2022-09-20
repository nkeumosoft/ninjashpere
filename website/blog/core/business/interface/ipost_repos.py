import abc
from typing import List

from blog.core.business.interface.imember import IMember
from blog.core.business.interface.ipost import IPost


class IPostRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, post_id: int) -> IPost:
        ...

    @abc.abstractmethod
    def find_by_title(self, title: str) -> List[IPost]:
        ...

    @abc.abstractmethod
    def find_by_author(self, author: IMember) -> List[IPost]:
        ...

    @abc.abstractmethod
    def create(self, post: IPost) -> None:
        ...

    @abc.abstractmethod
    def list(self) -> List[IPost]:
        ...

    @abc.abstractmethod
    def delete(self, post_id: int) -> None:
        ...

    @abc.abstractmethod
    def update(self, post_id: int, post_data: IPost) -> None:
        ...

    @abc.abstractmethod
    def count_likes(self, post_id: int) -> int:
        ...
