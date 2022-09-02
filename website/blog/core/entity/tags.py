import dataclasses
from uuid import UUID

from website.blog.core.interface.itags import ITags


@dataclasses.dataclass
class TagsEntity(ITags):
    uuid: UUID
    name: str
    description: str
    content: str

    def __init__(
        self, uuid: UUID, name: str, description: str, content: str
    ) -> None:
        self.uuid = uuid
        self.name = name
        self.description = description
        self.content = content

    @classmethod
    def factory(
        cls,
        uuid: UUID,
        name: str,
        description: str,
        content: str,
    ) -> ITags:
        object = cls(
            uuid=uuid, name=name, description=description, content=content
        )
        return object
