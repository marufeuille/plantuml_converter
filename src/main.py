from puml_converter.parser import PUmlTransformer
from puml_converter.transformer import ErToClassTransformer

with open("sample/test.pu") as f:
	puml = f.read()

print(PUmlTransformer(ErToClassTransformer).transform(puml))