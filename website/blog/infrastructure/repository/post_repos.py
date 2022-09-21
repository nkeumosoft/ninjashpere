from typing import List

from blog.core.business.entities import PostEntity, MemberEntity, KeyWordEntity
from blog.core.business.interface.ikeyword import IKeyWord
from blog.core.business.interface.imember import IMember
from blog.core.business.interface.ipost import IPost
from blog.core.business.interface.ipost_repos import IPostRepository
from blog.models import Post, Member, KeyWord


class PostRepository(IPostRepository):
    def __init__(self, post_model: Post, member_model: Member, keyword_model: KeyWord):
        self._post_model = post_model
        self._member_model = member_model
        self._keyword_model = keyword_model

    def find(self, post_id: int) -> IPost:
        instance = self._post_model.objects.get(id=post_id)
        return self._factory_post_entity(instance)

    def find_by_title(self, title: str) -> List[IPost]:
        instances = self._post_model.objects.filter(title__contains=title)
        return [self._factory_post_entity(instance) for instance in instances]

    def find_by_author(self, author: IMember) -> List[IPost]:
        user = self._member_model.objects.get(id=author.uuid)
        instances = self._post_model.objects.filter(author=user)
        return [self._factory_post_entity(instance) for instance in instances]

    def find_by_keyword(self, keyword: IKeyWord) -> List[IPost]:
        keyword = self._keyword_model.objects.get(id=keyword.id)
        instances = self._post_model.objects.filter(key_words__name=keyword.name)
        return [self._factory_post_entity(instance) for instance in instances]

    def find_by_type(self, post_type: str) -> List[IPost]:
        instances = self._post_model.objects.filter(post_type=post_type)
        return [self._factory_post_entity(instance) for instance in instances]

    def create(self, post: IPost) -> None:
        author = self._member_model.objects.get(id=post.author().uuid)
        self._post_model.objects.create(
            author=author,
            title=post.title,
            content=post.content,
            picture=post.picture,
            type=post.post_type,
        )

    def list(self) -> List[IPost]:
        instances = self._post_model.objects.all()
        return [self._factory_post_entity(instance) for instance in instances]

    def delete(self, post_id: int) -> None:
        self._post_model.objects.get(id=post_id).delete()

    def update(self, post_id: int, post_data: IPost) -> None:
        instance = self._post_model.objects.get(id=post_id)
        instance.title = post_data.title
        instance.content = post_data.content
        instance.picture = post_data.picture
        instance.save()

    def count_likes(self, post_id: int) -> int:
        instance = self._post_model.objects.get(id=post_id)
        return instance.likes.count()

    @staticmethod
    def _factory_post_entity(instance: Post) -> IPost:
        author = MemberEntity.factory(
            instance.author.user.last_name,
            instance.author.user.username,
            instance.author.user.password,
            instance.author.id,
        )
        keywords = {KeyWordEntity.factory(keyword.id, keyword.name) for keyword in instance.key_words.all()}

        return PostEntity.factory(
            id=instance.id,
            title=instance.title,
            content=instance.content,
            key_words=keywords,
            post_type=instance.post_type,
            author=author,
            picture=instance.picture,
            published_at=instance.published_at,
            updated_at=instance.updated_at,
            likes=instance.likes.count(),
        )
