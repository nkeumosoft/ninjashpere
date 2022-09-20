import abc
from typing import List

from blog.core.business.interface.icomment import IComment
from blog.core.business.interface.imember import IMember
from blog.core.business.interface.ipost import IPost


class ICommentRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, comment_id: int) -> IComment:
        ...

    @abc.abstractmethod
    def find_by_post(self, post: IPost) -> List[IComment]:
        ...

    @abc.abstractmethod
    def find_by_author(self, author: IMember) -> List[IComment]:
        ...

    @abc.abstractmethod
    def create(self, comment: IComment) -> None:
        ...

    @abc.abstractmethod
    def list(self) -> List[IComment]:
        ...

    @abc.abstractmethod
    def delete(self, comment_id: int) -> None:
        ...

    @abc.abstractmethod
    def update(self, comment_id: int, comment_data: IComment) -> None:
        ...

    @abc.abstractmethod
    def count_likes(self, comment_id: int) -> int:
        ...
