import typing
import json
import rubxy

from datetime import datetime
from enum import Enum

class Object:
    def __init__(self, client: "rubxy.Client" = None):
        self._client = client
    
    @staticmethod
    def default(obj: "Object"):
        if isinstance(obj, bytes):
            return repr(obj)
        
        if isinstance(obj, typing.Match):
            return repr(obj)

        if isinstance(obj, Enum):
            return str(obj)

        if isinstance(obj, datetime):
            return str(obj)
        
        attributes_to_hide = ()

        filtered_attributes = {
            attr: getattr(obj, attr)
            for attr in filter(
                lambda x: not x.startswith("_") and x not in attributes_to_hide,
                obj.__dict__,
            )
            if getattr(obj, attr) is not None
        }

        return dict(**filtered_attributes)
    
    def __str__(self) -> str:
        return json.dumps(self, indent=4, default=Object.default, ensure_ascii=False)
    
    def __getattr__(self, name):
        return None

class DictLike:
    def __repr__(self):
        return f"rubxy.types.{self.__class__.__name__}"
        
    def _to_dict(self):
        return self.__dict__