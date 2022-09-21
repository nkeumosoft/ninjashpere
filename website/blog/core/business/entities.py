from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Set
from uuid import UUID, uuid4

from blog.core.business.interface.icomment import IComment
from blog.core.business.interface.ikeyword import IKeyWord
from blog.core.business.interface.imember import IMember
from blog.core.business.interface.ipost import IPost


@dataclass
class MemberEntity(IMember):
    _name: str
    _email: str
    _password: str
    _uuid: UUID = field(default=uuid4())

    @property
    def uuid(self) -> UUID:
        return self._uuid

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def password(self) -> str:
        return self._password

    @classmethod
    def factory(
        cls,
        name: str,
        email: str,
        password: str,
        uuid: Optional[UUID] = None,
    ) -> "MemberEntity":
        uuid = uuid or uuid4()
        return cls(name, email, password, uuid)


@dataclass
class KeyWordEntity(IKeyWord):
    _name: str
    _id: int = field(default=-1)

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @classmethod
    def factory(cls, name: str, id=-1) -> "KeyWordEntity":
        return cls(name, id)


@dataclass
class PostEntity(IPost):
    _title: str
    _content: str
    _type: str
    _author: IMember
    _key_words: Set[IKeyWord] = field(default_factory=set)
    _picture: str = field(default="")
    _published_at: datetime = field(default_factory=datetime.now)
    _updated_at: datetime = field(default_factory=datetime.now)
    _likes: int = field(default=0)
    _id: int = field(default=-1)

    @property
    def id(self) -> int:
        return self._id

    @property
    def post_type(self) -> str:
        return self._type

    @property
    def title(self) -> str:
        return self._title

    # @title.setter
    # def title(self, title: str) -> None:
    #     self._title = title

    @property
    def content(self) -> str:
        return self._content

    # @content.setter
    # def content(self, content: str) -> None:
    #     self._content = content

    @property
    def picture(self) -> str:
        return self._picture

    # @picture.setter
    # def picture(self, picture: str) -> None:
    #     self._picture = picture

    @property
    def author(self) -> IMember:
        return self._author

    @property
    def key_words(self) -> Set[IKeyWord]:
        return self._key_words

    @property
    def published_at(self) -> datetime:
        return self._published_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    # @updated_at.setter
    # def updated_at(self, date: datetime) -> None:
    #     self._updated_at = date

    @property
    def likes(self) -> int:
        return self._likes

    @classmethod
    def factory(
        cls,
        title: str,
        content: str,
        post_type: str,
        author: IMember,
        key_words: Optional[Set[IKeyWord]] = None,
        picture: str = "",
        published_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        likes: int = 0,
        id: Optional[int] = None,
    ) -> "PostEntity":
        id = id or -1
        published_at = published_at or datetime.now()
        updated_at = updated_at or datetime.now()
        key_words = key_words or set()
        return cls(title, content, post_type, key_words, author, picture, published_at, updated_at, likes, id)


@dataclass
class CommentEntity(IComment):
    _author: IMember
    _content: str
    _post: IPost
    _published_at: datetime = field(default_factory=datetime.now)
    _updated_at: datetime = field(default_factory=datetime.now)
    _likes: int = field(default=0)
    _id: int = field(default=-1)

    @property
    def id(self) -> int:
        return self._id

    @property
    def content(self) -> str:
        return self._content

    # @content.setter
    # def content(self, content: str) -> None:
    #     self._content = content

    @property
    def author(self) -> IMember:
        return self._author

    @property
    def get_post(self) -> IPost:
        return self._post

    @property
    def published_at(self) -> datetime:
        return self._published_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    # @updated_at.setter
    # def updated_at(self, date: datetime) -> None:
    #     self._updated_at = date

    @property
    def likes(self) -> int:
        return self._likes

    @classmethod
    def factory(
        cls,
        author: IMember,
        content: str,
        post: IPost,
        published_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        likes: int = 0,
        id: Optional[int] = None,
    ) -> "CommentEntity":
        id = id or -1
        published_at = published_at or datetime.now()
        updated_at = updated_at or datetime.now()
        return cls(author, content, post, published_at, updated_at, likes, id)
