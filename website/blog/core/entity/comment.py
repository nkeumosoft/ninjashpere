import dataclasses
from dataclasses import field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from website.blog.core.interface.icomment import IComment


@dataclasses.dataclass
class CommentEntity(IComment):
    _author: Optional[UUID]
    _post: UUID
    _date_comment: datetime
    _content: str
    _likes: int
    _uuid: UUID = field(default=uuid4())

    def __init__(
        self,
        uuid: UUID,
        post: UUID,
        date_comment: datetime,
        content: str,
        likes: int,
        author: Optional[UUID],
    ):
        self._uuid = uuid4() or uuid
        self._author = author
        self._post = post
        self._date_comment = date_comment
        self._content = content
        self._likes = likes

    @property
    def likes(self) -> int:
        return self._likes

    @property
    def id(self):
        return self._uuid

    def author(self):
        return self._author

    @property
    def date_comment(self) -> str:
        return self._date_comment.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def content(self) -> str:
        return self._content

    @classmethod
    def factory(
        cls,
        uuid: UUID,
        post: UUID,
        date_comment: datetime,
        content: str,
        likes: int,
        author: Optional[UUID],
    ) -> IComment:
        author = None or author
        uuid = uuid4() or uuid
        obj = cls(
            uuid=uuid,
            post=post,
            date_comment=date_comment,
            content=content,
            likes=likes,
            author=author,
        )

        return obj
