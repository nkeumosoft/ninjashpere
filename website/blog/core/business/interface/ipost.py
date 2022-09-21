import abc
from datetime import datetime
from typing import Set

from blog.core.business.interface.ikeyword import IKeyWord
from blog.core.business.interface.imember import IMember


class IPost(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def id(self) -> int:
        ...

    @abc.abstractmethod
    def post_type(self) -> str:
        ...

    @abc.abstractmethod
    def title(self) -> str:
        ...

    @abc.abstractmethod
    def content(self) -> str:
        ...

    @abc.abstractmethod
    def key_words(self) -> Set[IKeyWord]:
        ...

    @abc.abstractmethod
    def picture(self) -> str:
        ...

    @abc.abstractmethod
    def author(self) -> IMember:
        ...

    @abc.abstractmethod
    def published_at(self) -> datetime:
        ...

    @abc.abstractmethod
    def updated_at(self) -> datetime:
        ...

    @abc.abstractmethod
    def likes(self) -> int:
        ...
