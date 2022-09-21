from typing import List

from blog.core.business.entities import KeyWordEntity
from blog.core.business.interface.ikeyword import IKeyWord
from blog.core.business.interface.ikeyword_repos import IKeyWordRepository
from blog.models import KeyWord


class KeyWordRepository(IKeyWordRepository):
    def __init__(self, model: KeyWord):
        self._model = model

    def find(self, id: int) -> IKeyWord:
        instance = self._model.objects.get(id=id)
        return self._factory_keyword_entity(instance)

    def find_by_name(self, name: str) -> IKeyWord:
        instance = self._model.objects.get(name=name)
        return self._factory_keyword_entity(instance)

    def create(self, key_word: IKeyWord) -> None:
        self._model.objects.create(name=key_word.name)

    def list(self) -> List[IKeyWord]:
        instances = self._model.objects.all()
        return [self._factory_keyword_entity(instance) for instance in instances]

    def delete(self, id: int) -> None:
        self._model.objects.get(id=id).delete()

    @staticmethod
    def _factory_keyword_entity(instance: KeyWord) -> IKeyWord:
        return KeyWordEntity.factory(id=instance.id, name=instance.name)
