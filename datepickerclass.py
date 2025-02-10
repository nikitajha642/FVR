from base import BaseClass
from datetime import datetime


class DatePickerClass(BaseClass):
    def __init__(
        self,
        label,
        name,
        required=False,
        value=None,
        min_date=None,
        max_date=None,
        date_format="%Y-%m-%d",
        className="form-control",
    ):

        self.date_format = date_format
        self.value = self._parse_date(value) if value else None
        self.min_date = self._parse_date(min_date) if min_date else None
        self.max_date = self._parse_date(max_date) if max_date else None

        # Validate the date before calling the parent constructor
        if self.value and not self.validate_date():
            raise ValueError(
                f"Invalid date '{self.value.strftime(self.date_format)}'. "
                f"Must be between '{self.min_date}' and '{self.max_date}'."
            )

        # Call the parent constructor
        super().__init__(
            field_type="date",
            label=label,
            name=name,
            required=required,
            value=self.value.strftime(self.date_format) if self.value else None,
            className=className,
        )

    def _parse_date(self, date_str):
        """Parses a string into a datetime object based on the given format."""
        try:
            return datetime.strptime(date_str, self.date_format)
        except ValueError:
            raise ValueError(
                f"Invalid date format: '{date_str}'. Expected format: '{self.date_format}'."
            )

    def validate_date(self):
        """
        Validates if the selected date is within the allowed range.
        """
        if self.value is None:
            return True  # If no value is given, no validation needed

        if self.min_date and self.value < self.min_date:
            return False  # The date is earlier than the minimum allowed date

        if self.max_date and self.value > self.max_date:
            return False  # The date is later than the maximum allowed date

        return True

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["min_date"] = (
            self.min_date.strftime(self.date_format) if self.min_date else None
        )
        base_dict["max_date"] = (
            self.max_date.strftime(self.date_format) if self.max_date else None
        )
        return base_dict

date_picker = DatePickerClass(
    label="Select Date",
    name="date",
    required=True,
    value="2025-02-15",
    min_date="2001-01-01",
    max_date="2025-12-31",
)

print(date_picker.to_dict())