import abc
from typing import List
from uuid import UUID

from website.blog.core.entity.article import ArticleEntity
from website.blog.core.interface.iarticle import IArticle
from website.blog.infrastructure.interface.iarticle_repo import (
    IArticleRepository,
)
from website.blog.infrastructure.repository.member_repo import MemberRepository
from website.blog.models import Post


class ArticleRepository(IArticleRepository):
    def __init__(self, model: Post, mem_repo: MemberRepository):
        self._model = model
        self.memer_repo = mem_repo

    @property
    def model(self):
        return self._model.objects

    @abc.abstractmethod
    def find(self, uuid: UUID) -> IArticle:
        return self._factory_article(self.model.get(uuid=uuid))

    @abc.abstractmethod
    def find_by_name(self, name: str) -> IArticle:
        article = self.model.get(title=name)
        return self._factory_article(article)

    @abc.abstractmethod
    def find_by_tags(self, tags: UUID) -> IArticle:
        ...

    @abc.abstractmethod
    def update(self, article: IArticle) -> IArticle:
        ...

    @abc.abstractmethod
    def create(self, article: IArticle) -> IArticle:
        ...

    @abc.abstractmethod
    def list(self) -> List[IArticle]:
        ...

    def picture(self, uuid: UUID):
        article_pict = self.model.get(uuid=uuid)
        picture = article_pict.picture.url
        return picture

    def get_author(self, uuid: UUID) -> UUID:
        author = self.model.get(uuid=uuid).author
        return author

    def _factory_article(self, article: Post) -> IArticle:
        article_entiy = ArticleEntity.factory(
            uuid=article.uuid,
            title=article.title,
            content=article.content,
            picture=self.picture(article.uuid),
            author=self.get_author(article.author.uuid),
            publish_date=article.publish_date,
            last_edit=article.last_edit,
            likes=article.likes,
            publish=article.publish,
        )

        return article_entiy
