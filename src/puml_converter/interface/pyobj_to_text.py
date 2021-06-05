from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic

from puml_converter.interface.intermediate import PyObj

T = TypeVar('T', bound=PyObj)
class PyObjToTextTransformer(Generic[T],metaclass=ABCMeta):
    @abstractmethod
    def transform_to_text(self, input: T) -> str:
        pass