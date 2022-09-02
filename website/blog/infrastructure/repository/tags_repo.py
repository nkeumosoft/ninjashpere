from uuid import UUID

from website.blog.core.entity.tags import TagsEntity
from website.blog.core.interface.itags import ITags


class TagsRepository(ITags):
    def find(self, uuid: UUID) -> ITags:
        pass

    def find_by_name(self, name: str) -> ITags:
        pass

    def find_by_tags(self, tags: UUID) -> ITags:
        pass

    def create(self, article: ITags) -> ITags:
        pass

    def _factory_article(self, article) -> TagsEntity:
        pass
