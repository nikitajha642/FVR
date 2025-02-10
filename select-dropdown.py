from base import BaseClass

class SelectDropDown(BaseClass):
    def __init__(self, label, name, required=False, value=None, options=None, className="form-select"):
        super().__init__(field_type="select", label=label, name=name, required=required, value=value, className=className)
        self.options = options if options else []  

    def to_dict(self):
        base_dict = super().to_dict()  
        base_dict["options"] = self.options 
        return base_dict


dropdown_field = SelectDropDown(
    label="Choose your country",
    name="country",
    required=True,
    options=[
        {"value": "us", "label": "United States"},
        {"value": "uk", "label": "United Kingdom"},
        {"value": "ca", "label": "Canada"},
    ],
)

print(dropdown_field.to_dict())
