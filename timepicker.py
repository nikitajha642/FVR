from base import BaseClass
from datetime import datetime


class TimePickerClass(BaseClass):
    def __init__(
        self,
        label,
        name,
        required=False,
        value=None,
        min_time=None,
        max_time=None,
        time_format="%H:%M:%S",
        className="form-control",
    ):

        self.time_format = time_format
        self.value = self._parse_time(value) if value else None
        self.min_time = self._parse_time(min_time) if min_time else None
        self.max_time = self._parse_time(max_time) if max_time else None

        # Validate the time before calling the parent constructor
        if self.value and not self.validate_time():
            raise ValueError(
                f"Invalid time '{self.value.strftime(self.time_format)}'. "
                f"Must be between '{self.min_time.strftime(self.time_format) if self.min_time else None}' "
                f"and '{self.max_time.strftime(self.time_format) if self.max_time else None}'."
            )

        # Call the parent constructor
        super().__init__(
            field_type="time",
            label=label,
            name=name,
            required=required,
            value=self.value.strftime(self.time_format) if self.value else None,
            className=className,
        )

    def _parse_time(self, time_str):
        
        if time_str is None:
            return None
        try:
            return datetime.strptime(time_str, self.time_format).time()
        except ValueError:
            raise ValueError(
                f"Invalid time format: '{time_str}'. Expected format: '{self.time_format}'."
            )

    def validate_time(self):
        
        if self.value is None:
            return True  

        if self.min_time and self.value < self.min_time:
            return False  
        if self.max_time and self.value > self.max_time:
            return False  
        return True

    def to_dict(self):
        """Returns the object data as a dictionary."""
        base_dict = super().to_dict()
        base_dict["min_time"] = (
            self.min_time.strftime(self.time_format) if self.min_time else None
        )
        base_dict["max_time"] = (
            self.max_time.strftime(self.time_format) if self.max_time else None
        )
        return base_dict

time_picker = TimePickerClass(
    label="Select Time",
    name="time",
    required=True,
    value="14:30:00",
    min_time="08:00:00",
    max_time="18:00:00",
)
print(time_picker.to_dict())
