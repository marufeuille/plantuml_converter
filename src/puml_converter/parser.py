from typing import Any, List, Type
from lark import Lark, Transformer

class PUmlTransformer:
	def __init__(self, transformer_class:Type[Transformer], grammer_file:str="src/grammer_plantuml.lark", debug:bool = False):
		with open(grammer_file) as grammar:
			self._parser = Lark(grammar.read(), start="uml")
		self._transformer_class = transformer_class
		self._debug = debug

	def transform(self, input_puml_str: str):
		tree = self._parser.parse(input_puml_str)
		if self._debug:
			print(tree.pretty())
		self._tran = self._transformer_class()
		return self._tran.transform(tree)