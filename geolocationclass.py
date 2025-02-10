from base import BaseClass


class GeolocationClass(BaseClass):
    def __init__(
        self,
        label,
        name,
        required=False,
        value=None,
        latitude=None,
        longitude=None,
        className="form-control",
    ):
        # Convert latitude and longitude to float if they are not None
        self.latitude = float(latitude) if latitude is not None else None
        self.longitude = float(longitude) if longitude is not None else None

        # Validate the coordinates before creating the instance
        if not self.validate_coordinates():
            raise ValueError(
                f"Invalid latitude ({self.latitude}) or longitude ({self.longitude}). "
                "Latitude must be between -90 and 90, and longitude must be between -180 and 180."
            )

        # Call the parent constructor after validation
        super().__init__(
            field_type="geolocation",
            label=label,
            name=name,
            required=required,
            value=value,
            className=className,
        )

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["latitude"] = self.latitude
        base_dict["longitude"] = self.longitude
        return base_dict

    def validate_coordinates(self):
        """
        Validates if latitude and longitude are within valid ranges.
        - Latitude: -90 to 90
        - Longitude: -180 to 180
        """
        if self.latitude is None or self.longitude is None:
            return False  # Both coordinates must be provided

        if not (-90 <= self.latitude <= 90):
            return False  # Latitude must be between -90 and 90

        if not (-180 <= self.longitude <= 180):
            return False  # Longitude must be between -180 and 180

        return True


# Testing with Invalid Coordinates
try:
    geo_field = GeolocationClass(
        label="Search my location",
        name="maps",
        required=True,
        latitude=-100,  # Invalid latitude
        longitude=-18000,  # Invalid longitude
    )
    print(f"Are the coordinates valid? {geo_field.validate_coordinates()}")
    print(geo_field.to_dict())

except ValueError as e:
    print(f"Error: {e}")
