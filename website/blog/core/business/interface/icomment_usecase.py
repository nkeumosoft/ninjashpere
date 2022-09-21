import abc
from typing import List
from uuid import UUID

from blog.core.business.interface.icomment import IComment


class ICommentUseCase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_comment(self, content: str, author_id: UUID, post_id: int) -> None:
        ...

    @abc.abstractmethod
    def list_comments(self) -> List[IComment]:
        ...

    @abc.abstractmethod
    def update_comment(self, comment_id: int, content: str) -> None:
        ...

    @abc.abstractmethod
    def delete_comment(self, comment_id: int) -> None:
        ...

    @abc.abstractmethod
    def get_comment(self, comment_id: int) -> IComment:
        ...

    @abc.abstractmethod
    def get_comments_by_author(self, author_id: UUID) -> List[IComment]:
        ...

    @abc.abstractmethod
    def get_comments_by_post(self, post_id: int) -> List[IComment]:
        ...

    @abc.abstractmethod
    def get_comment_likes(self, comment_id: int) -> int:
        ...

    @abc.abstractmethod
    def like_comment(self, comment_id: int) -> None:
        ...

    @abc.abstractmethod
    def unlike_comment(self, comment_id: int) -> None:
        ...
