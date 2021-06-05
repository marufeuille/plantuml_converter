from typing import List
from puml_converter.interface import PyObjToTextTransformer, LarkPyObj


_type_map = {
    "STRING": "str",
    "INTEGER": "int"
}

class PyObjToDataClassTransformer(PyObjToTextTransformer[LarkPyObj]):
    def __init__(self) -> None:
        super().__init__()

    def transform_to_text(self, input: LarkPyObj) -> str:
        class_name = f'{input.root["name"].capitalize()}Entity:\n'
        fields: List[str] = []
        for field_schema in input.root["table_field_schema"]:
            fields.append(f'    {field_schema["name"]}: {_type_map[field_schema["type"]]}')

        return "from dataclasses import dataclass\n\n\n@dataclass\n" + class_name + '\n'.join(fields)
