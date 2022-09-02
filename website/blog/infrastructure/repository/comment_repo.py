from uuid import UUID

from website.blog.core.entity.comment import CommentEntity
from website.blog.core.interface.icomment import IComment
from website.blog.infrastructure.interface.icomment_repo import (
    ICommentRepository,
)
from website.blog.models import Comment


class CommentRepository(ICommentRepository):
    def find(self, uuid: UUID) -> IComment:
        pass

    def find_by_name(self, name: str) -> IComment:
        pass

    def find_by_tags(self, tags: UUID) -> IComment:
        pass

    def update(self, article: IComment) -> IComment:
        pass

    def create(self, article: IComment, uuid: UUID) -> IComment:
        pass

    def get_author(self, uuid: UUID) -> UUID:
        pass

    def get_post(self, uuid: UUID) -> UUID:
        pass

    def factory(self, comment: Comment) -> IComment:
        obj = CommentEntity.factory(
            uuid=comment.uuid,
            post=self.get_post(comment.uuid),
            date_comment=comment.date_comment,
            content=comment.content,
            likes=comment.likes,
            author=self.get_author(comment.uuid),
        )

        return obj
