import re
from datetime import datetime


class BaseClass():
    def __init__(self,field_type,label,name,required=False,value=None,subtype=None,access=True,className="form-control",):
        self.type = field_type
        self.label = label
        self.name = name
        self.required = required
        self.value = value
        self.subtype = subtype
        self.access = access
        self.className = className

    def to_dict(self):
        return {
            "type": self.type,
            "label": self.label,
            "name": self.name,
            "required": self.required,
            "value": self.value,
            "subtype": self.subtype,
            "access": self.access,
            "className": self.className,
        }
