import abc
from typing import List

from blog.core.business.interface.ikeyword import IKeyWord


class IKeyWordRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, id: int) -> IKeyWord:
        ...

    @abc.abstractmethod
    def find_by_name(self, name: str) -> IKeyWord:
        ...

    @abc.abstractmethod
    def create(self, key_word: IKeyWord) -> None:
        ...

    @abc.abstractmethod
    def list(self) -> List[IKeyWord]:
        ...

    @abc.abstractmethod
    def delete(self, id: int) -> None:
        ...
