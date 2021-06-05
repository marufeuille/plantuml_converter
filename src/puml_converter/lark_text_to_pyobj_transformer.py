from dataclasses import dataclass
from typing import Dict, Type

from lark import Lark, Transformer
import injector

from puml_converter.interface import LarkPyObj, TextToPyObjTransformer


class LarkTextToPyObjTransformer(TextToPyObjTransformer[LarkPyObj]):
    @injector.inject
    def __init__(self, lark_transformer_class:Type[Transformer], lark_grammer:str, debug:bool = False):
        self._parser = Lark(lark_grammer, start="uml")
        self._lark_transformer_class = lark_transformer_class
        self._debug = debug

    def transform_to_pyobject(self, input_str: str) -> LarkPyObj:
        tree = self._parser.parse(input_str)
        if self._debug:
            print(tree.pretty())
        self._tran = self._lark_transformer_class()
        return LarkPyObj(root=self._tran.transform(tree))