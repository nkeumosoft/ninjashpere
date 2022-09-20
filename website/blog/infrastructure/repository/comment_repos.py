from typing import List

from blog.core.business.entities import MemberEntity, PostEntity, CommentEntity
from blog.core.business.interface.icomment import IComment
from blog.core.business.interface.icomment_repos import ICommentRepository
from blog.core.business.interface.imember import IMember
from blog.core.business.interface.ipost import IPost
from blog.models import Comment, Post, Member


class CommentRepository(ICommentRepository):
    def __init__(self, comment_model: Comment, member_model: Member, post_model: Post):
        self._comment_model = comment_model
        self._member_model = member_model
        self._post_model = post_model

    def find(self, comment_id: int) -> IComment:
        instance = self._comment_model.objects.get(id=comment_id)
        return self._factory_comment_entity(instance)

    def find_by_post(self, post: IPost) -> List[IComment]:
        post_instance = self._post_model.objects.get(id=post.id)
        instances = self._comment_model.objects.filter(post=post_instance)
        return [self._factory_comment_entity(instance) for instance in instances]

    def find_by_author(self, author: IMember) -> List[IComment]:
        author_instance = self._member_model.objects.get(id=author.uuid)
        instances = self._comment_model.objects.filter(author=author_instance)
        return [self._factory_comment_entity(instance) for instance in instances]

    def create(self, comment: IComment) -> None:
        post = self._post_model.objects.get(id=comment.get_post().id)
        author = self._member_model.objects.get(id=comment.author().uuid)
        self._comment_model.objects.create(
            author=author,
            post=post,
            content=comment.content,
        )

    def list(self) -> List[IComment]:
        instances = self._comment_model.objects.all()
        return [self._factory_comment_entity(instance) for instance in instances]

    def delete(self, comment_id: int) -> None:
        self._comment_model.objects.get(id=comment_id).delete()

    def update(self, comment_id: int, comment_data: IComment) -> None:
        instance = self._comment_model.objects.get(id=comment_id)
        instance.content = comment_data.content
        instance.save()

    def count_likes(self, comment_id: int) -> int:
        instance = self._comment_model.objects.get(id=comment_id)
        return instance.likes.count()

    @staticmethod
    def _factory_comment_entity(instance: Comment) -> IComment:
        comment_author = MemberEntity.factory(
            name=instance.author.user.last_name,
            email=instance.author.user.username,
            password=instance.author.user.password,
            uuid=instance.author.id,
        )
        post_author = MemberEntity.factory(
            name=instance.post.author.user.last_name,
            email=instance.post.author.user.username,
            password=instance.post.author.user.password,
            uuid=instance.post.author.id,
        )
        post = PostEntity.factory(
            title=instance.post.title,
            content=instance.post.content,
            picture=instance.post.picture,
            author=post_author,
            id=instance.post.id,
            published_at=instance.post.published_at,
            updated_at=instance.post.updated_at,
            likes=instance.post.likes.count(),
        )
        return CommentEntity.factory(
            id=instance.id,
            author=comment_author,
            content=instance.content,
            post=post,
            published_at=instance.published_at,
            updated_at=instance.updated_at,
            likes=instance.likes.count(),
        )
