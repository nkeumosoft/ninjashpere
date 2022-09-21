from dataclasses import dataclass
from typing import List
from uuid import UUID

from blog.core.business.entities import CommentEntity
from blog.core.business.interface.icomment import IComment
from blog.core.business.interface.icomment_repos import ICommentRepository
from blog.core.business.interface.icomment_usecase import ICommentUseCase
from blog.core.business.interface.imember_repos import IMemberRepository
from blog.core.business.interface.ipost_repos import IPostRepository


@dataclass
class CommentManagement(ICommentUseCase):
    _comment_repository: ICommentRepository
    _member_repository: IMemberRepository
    _post_repository: IPostRepository

    def create_comment(self, content: str, author_id: UUID, post_id: int) -> None:
        post = self._post_repository.find(post_id)
        author = self._member_repository.find(author_id)
        comment = CommentEntity.factory(author, content, post)
        self._comment_repository.create(comment)

    def list_comments(self) -> List[IComment]:
        return self._comment_repository.list()

    def update_comment(self, comment_id: int, content: str) -> None:
        comment = self._comment_repository.find(comment_id)
        new_comment = CommentEntity.factory(comment.author, content, comment.get_post)
        self._comment_repository.update(comment_id, new_comment)

    def delete_comment(self, comment_id: int) -> None:
        self._comment_repository.delete(comment_id)

    def get_comment(self, comment_id: int) -> IComment:
        return self._comment_repository.find(comment_id)

    def get_comments_by_author(self, author_id: UUID) -> List[IComment]:
        author = self._member_repository.find(author_id)
        return self._comment_repository.find_by_author(author)

    def get_comments_by_post(self, post_id: int) -> List[IComment]:
        post = self._post_repository.find(post_id)
        return self._comment_repository.find_by_post(post)

    def get_comment_likes(self, comment_id: int) -> int:
        return self._comment_repository.count_likes(comment_id)

    def like_comment(self, comment_id: int) -> None:
        pass

    def unlike_comment(self, comment_id: int) -> None:
        pass
