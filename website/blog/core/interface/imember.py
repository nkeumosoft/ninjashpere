import abc
import dataclasses
from datetime import datetime
from uuid import UUID


@dataclasses.dataclass
class IMember(metaclass=abc.ABCMeta):
    uuid: UUID
    name: str
    email: str
    password: str
    is_staff: bool
    is_active: bool
    date_joined: datetime

    @classmethod
    def factory(
        cls,
        uuid: UUID,
        name: str,
        email: str,
        password: str,
        is_staff: bool,
        is_active: bool,
        date_joined: datetime,
    ) -> "IMember":
        pass
