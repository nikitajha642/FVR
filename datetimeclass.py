from base import BaseClass


class DateTimePickerClass(BaseClass):
    def __init__(
        self,
        label,
        name,
        required=False,
        value=None,
        min_datetime=None,
        max_datetime=None,
        datetime_format="%Y-%m-%d %H:%M:%S",
        className="form-control",
    ):
        """
        Initializes a DateTime picker field.

        :param label: The label for the field.
        :param name: The name of the field.
        :param required: Whether the field is required.
        :param value: The default selected datetime (string format).
        :param min_datetime: The minimum allowed datetime.
        :param max_datetime: The maximum allowed datetime.
        :param datetime_format: The format of the datetime.
        :param className: The CSS class for styling.
        """

        # Convert string datetimes to datetime objects
        self.datetime_format = datetime_format
        self.value = self._parse_datetime(value) if value else None
        self.min_datetime = self._parse_datetime(min_datetime) if min_datetime else None
        self.max_datetime = self._parse_datetime(max_datetime) if max_datetime else None

        # Validate the datetime before calling the parent constructor
        if self.value and not self.validate_datetime():
            raise ValueError(
                f"Invalid datetime '{self.value.strftime(self.datetime_format)}'. "
                f"Must be between '{self.min_datetime}' and '{self.max_datetime}'."
            )

        # Call the parent constructor
        super().__init__(
            field_type="datetime",
            label=label,
            name=name,
            required=required,
            value=self.value.strftime(self.datetime_format) if self.value else None,
            className=className,
        )

    def _parse_datetime(self, datetime_str):
        """Parses a string into a datetime object based on the given format."""
        try:
            return datetime.strptime(datetime_str, self.datetime_format)
        except ValueError:
            raise ValueError(
                f"Invalid datetime format: '{datetime_str}'. Expected format: '{self.datetime_format}'."
            )

    def validate_datetime(self):
        """
        Validates if the selected datetime is within the allowed range.
        """
        if self.value is None:
            return True  # If no value is given, no validation needed

        if self.min_datetime and self.value < self.min_datetime:
            return False  # The datetime is earlier than the minimum allowed datetime

        if self.max_datetime and self.value > self.max_datetime:
            return False  # The datetime is later than the maximum allowed datetime

        return True

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["min_datetime"] = (
            self.min_datetime.strftime(self.datetime_format)
            if self.min_datetime
            else None
        )
        base_dict["max_datetime"] = (
            self.max_datetime.strftime(self.datetime_format)
            if self.max_datetime
            else None
        )
        return base_dict


datetime_picker = DateTimePickerClass(
    label="Select Date & Time",
    name="datetime",
    required=True,
    value="2025-02-15 14:30:00",
    min_datetime="2025-01-01 00:00:00",
    max_datetime="2025-12-31 23:59:59",
)
print(datetime_picker.to_dict())
