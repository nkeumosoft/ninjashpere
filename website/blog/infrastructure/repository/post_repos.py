from typing import List

from blog.core.business.entities import PostEntity, MemberEntity
from blog.core.business.interface.imember import IMember
from blog.core.business.interface.ipost import IPost
from blog.core.business.interface.ipost_repos import IPostRepository
from blog.models import Post, Member


class PostRepository(IPostRepository):
    def __init__(self, post_model: Post, member_model: Member):
        self._post_model = post_model
        self._member_model = member_model

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

    def create(self, post: IPost) -> None:
        author = self._member_model.objects.get(id=post.author().uuid)
        self._post_model.objects.create(
            author=author,
            title=post.title,
            content=post.content,
            picture=post.picture,
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
        return PostEntity.factory(
            id=instance.id,
            title=instance.title,
            content=instance.content,
            author=author,
            picture=instance.picture,
            published_at=instance.published_at,
            updated_at=instance.updated_at,
            likes=instance.likes.count(),
        )
