from typing import List, Union
from lark import Transformer, Token, Tree

class ErToClassTransformer(Transformer):

    def uml(self, tree:List[Union[Tree, Token]]):
        return tree[1]

    def start_uml(self, tree:List[Union[Tree, Token]]):
        return None

    def end_uml(self, tree:List[Union[Tree, Token]]):
        return None

    def entity(self, tree: List[Union[Tree, Token]]):
        entity = {
            "name": "",
            "table_field_schema": []
        }
        for node in tree:
            if type(node) is Tree:
                if node.data == "entity_sym":
                    pass
                if node.data == "identifier":
                    entity["name"] = node.children[0].value
                if node.data == "table_field_schema":
                    entity["table_field_schema"].append(self._table_field_schema(node.children))
        return entity

    def _table_field_schema(self, tree: List[Union[Tree, Token]]):
        table_field_schema = {
            "name": "",
            "type": "",
            "mandatory": False,
            "pk": False,
            "FK": False
        }
        
        for node in tree:
            if type(node) is Tree:
                if node.data == "mandatory_flag":
                    table_field_schema["mandatory"] = True
                if node.data == "identifier":
                    ident = node.children[0].value.upper()
                    if ident in ("INTEGER", "STRING", "DATE", ):
                        table_field_schema["type"] = ident
                    elif ident == "FK":
                        table_field_schema["FK"] = True
                    elif ident == "PK":
                        table_field_schema["PK"] = True
                    else:
                        table_field_schema["name"] = node.children[0].value
        return table_field_schema