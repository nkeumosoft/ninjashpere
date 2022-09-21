import abc


class IKeyWord(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def id(self) -> int:
        ...

    @abc.abstractmethod
    def name(self) -> str:
        ...
