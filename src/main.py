from puml_converter import LarkTextToPyObjTransformer
from puml_converter import ErToPyObjLarkTransformer
from puml_converter.pyobj_to_dataclass import PyObjToDataClassTransformer

with open("sample/test.pu") as f:
    puml = f.read()


with open("src/grammer_plantuml.lark") as f:
    grammer = f.read()

pyobj = LarkTextToPyObjTransformer(
        lark_transformer_class=ErToPyObjLarkTransformer, lark_grammer=grammer
    ).transform_to_pyobject(puml)
print(pyobj)

dataclass_str = PyObjToDataClassTransformer().transform_to_text(pyobj)
print(dataclass_str)