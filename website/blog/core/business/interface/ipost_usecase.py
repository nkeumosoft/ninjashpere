import abc
from typing import List
from uuid import UUID

from blog.core.business.interface.ipost import IPost


class IPostUseCase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_post(self, title: str, content: str, author_id: UUID) -> None:
        ...

    @abc.abstractmethod
    def list_posts(self) -> List[IPost]:
        ...

    @abc.abstractmethod
    def update_post(self, post_id: int, title: str, content: str, picture: str) -> None:
        ...

    @abc.abstractmethod
    def delete_post(self, post_id: int) -> None:
        ...

    @abc.abstractmethod
    def get_post(self, post_id: int) -> IPost:
        ...

    @abc.abstractmethod
    def get_posts_by_title(self, title: str) -> List[IPost]:
        ...

    @abc.abstractmethod
    def get_posts_by_author(self, author_id: UUID) -> List[IPost]:
        ...

    @abc.abstractmethod
    def get_post_likes(self, post_id: int) -> None:
        ...

    @abc.abstractmethod
    def like_post(self, post_id: int) -> None:
        ...

    @abc.abstractmethod
    def unlike_post(self, post_id: int) -> None:
        ...
