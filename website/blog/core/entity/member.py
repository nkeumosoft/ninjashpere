from datetime import datetime
from uuid import UUID

from website.blog.core.interface.imember import IMember


class MemberEntity(IMember):
    uuid: UUID
    name: str
    email: str
    password: str
    is_staff: bool
    is_active: bool
    date_joined: datetime

    def __init__(
        self,
        uuid: UUID,
        name: str,
        email: str,
        password: str,
        is_staff: bool,
        is_active: bool,
        date_joined: datetime,
    ):
        self.uuid = uuid
        self.name = name
        self.email = email
        self.password = password
        self.is_staff = is_staff
        self.is_active = is_active
        self.date_joined = date_joined

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
    ) -> IMember:
        member = cls(
            uuid=uuid,
            name=name,
            email=email,
            password=password,
            is_active=is_active,
            date_joined=date_joined,
            is_staff=is_staff,
        )
        return member
