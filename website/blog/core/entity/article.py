import dataclasses
from datetime import datetime
from uuid import UUID

from website.blog.core.interface.iarticle import IArticle


@dataclasses.dataclass
class ArticleEntity(IArticle):
    _uuid: UUID
    _title: str
    _content: str
    _picture: str
    _author: UUID
    _publish_date: datetime
    _last_edit: datetime
    _likes: int = dataclasses.field(default=0)
    _publish: bool = dataclasses.field(default=True)

    def __init__(
        self,
        title,
        content,
        picture,
        author,
        publish_date,
        last_edit,
        likes,
        publish,
    ):
        self._title = title
        self._content = content
        self._picture = picture
        self._author = author
        self._publish_date = publish_date
        self._last_edit = last_edit
        self._likes = likes
        self._publish = publish

    @property
    def id(self):
        return self._uuid

    @property
    def title(self):
        return self._title

    def content(self):
        return self._content

    @property
    def picture(self):
        return self._picture.url

    @property
    def author(self):
        return self._author

    @property
    def publish(self) -> bool:
        publish = self._publish
        return publish

    @property
    def publish_date(self) -> str:
        return self._publish_date.strftime("%d/%m/%Y")

    @property
    def last_edit(self):
        return self._last_edit.strftime("%d/%m/%Y")

    @property
    def likes(self):
        return self._likes

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
        obj = cls(
            title=title,
            content=content,
            picture=picture,
            author=author,
            publish_date=publish_date,
            last_edit=last_edit,
            likes=likes,
            publish=publish,
        )
        return obj
