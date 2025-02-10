from base import BaseClass


import re


class AutocompleteClass(BaseClass):

    def __init__(
        self,
        label,
        name,
        required=False,
        value=None,
        options=None,
        className="form-select",
    ):
        super().__init__(
            field_type="select",
            label=label,
            name=name,
            required=required,
            value=value,
            className=className,
        )
        self.options = options if options else []

    

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["options"] = self.options
        return base_dict

    def filter_options(self, query):
        
        return [
            option
            for option in self.options
            if re.search(query, option["label"], re.IGNORECASE)
        ]

    def to_dict(self, query=None):
        base_dict = super().to_dict()  # Get base class attributes
        if query:
            # Filter options based on the query before returning the dictionary
            filtered_options = self.filter_options(query)
            base_dict["options"] = filtered_options
        return base_dict


# Example usage
autocomplete_field = AutocompleteClass(
    label="Search for your country",
    name="country",
    required=True,
    options=[
        {"value": "us", "label": "United States"},
        {"value": "uk", "label": "United Kingdom"},
        {"value": "ca", "label": "Canada"},
        {"value": "de", "label": "Germany"},
        {"value": "fr", "label": "France"},
    ],
)


search_query = "fr"  # This is what the user typed (simulate user input)
print(autocomplete_field.to_dict(query=search_query))
