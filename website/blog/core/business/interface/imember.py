import abc
from uuid import UUID


class IMember(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def uuid(self) -> UUID:
        ...

    @abc.abstractmethod
    def name(self) -> str:
        ...

    @abc.abstractmethod
    def email(self) -> str:
        ...

    @abc.abstractmethod
    def password(self) -> str:
        ...
