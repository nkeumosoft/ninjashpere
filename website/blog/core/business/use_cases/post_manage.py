from dataclasses import dataclass
from typing import List
from uuid import UUID

from blog.core.business.entities import PostEntity
from blog.core.business.interface.imember_repos import IMemberRepository
from blog.core.business.interface.ipost import IPost
from blog.core.business.interface.ipost_repos import IPostRepository
from blog.core.business.interface.ipost_usecase import IPostUseCase


@dataclass
class PostManagement(IPostUseCase):
    _post_repository: IPostRepository
    _member_repository: IMemberRepository

    def create_post(self, title: str, content: str, author_id: UUID) -> None:
        author = self._member_repository.find(author_id)
        post = PostEntity.factory(title, content, author)
        self._post_repository.create(post)

    def list_posts(self) -> List[IPost]:
        return self._post_repository.list()

    def update_post(self, post_id: int, title: str, content: str, picture: str) -> None:
        post = self._post_repository.find(post_id)
        updated_post_data = PostEntity.factory(title, content, post.author(), picture)
        self._post_repository.update(post_id, updated_post_data)

    def delete_post(self, post_id: int) -> None:
        self._post_repository.delete(post_id)

    def get_post(self, post_id: int) -> IPost:
        return self._post_repository.find(post_id)

    def get_posts_by_title(self, title: str) -> List[IPost]:
        return self._post_repository.find_by_title(title)

    def get_posts_by_author(self, author_id: UUID) -> List[IPost]:
        member = self._member_repository.find(author_id)
        return self._post_repository.find_by_author(member)

    def get_post_likes(self, post_id: int) -> int:
        return self._post_repository.count_likes(post_id)

    def like_post(self, post_id: int) -> None:
        pass

    def unlike_post(self, post_id: int) -> None:
        pass
