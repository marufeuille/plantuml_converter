from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from puml_converter.interface.intermediate import PyObj

T = TypeVar('T', bound=PyObj)

class TextToPyObjTransformer(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def transform_to_pyobject(self, input_str: str) -> T:
        pass
