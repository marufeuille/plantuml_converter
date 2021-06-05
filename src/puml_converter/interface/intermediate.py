from dataclasses import dataclass
from typing import Dict

@dataclass
class PyObj:
    pass

@dataclass
class LarkPyObj(PyObj):
    root: Dict
