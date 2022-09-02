import abc
from uuid import UUID


class ITags(metaclass=abc.ABCMeta):
    uuid: UUID
    name: str
    description: str
    content: str

    @classmethod
    def factory(
        cls,
        uuid: UUID,
        name: str,
        description: str,
        content: str,
    ) -> "ITags":
        ...
