from base import BaseClass


from base import BaseClass
import os


class ImageUploadClass(BaseClass):
    ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif"}  # Allowed image formats

    def __init__(
        self,
        label,
        name,
        required=False,
        value=None,
        upload_type="gallery",  # Options: "gallery", "camera", "location"
        latitude=None,
        longitude=None,
        max_file_size=5,  # Max file size in MB
        className="form-control",
    ):
       

        self.upload_type = upload_type.lower()
        self.latitude = latitude
        self.longitude = longitude
        self.max_file_size = max_file_size  # MB

        # Validate upload type
        if self.upload_type not in {"gallery", "camera", "location"}:
            raise ValueError(
                f"Invalid upload type '{self.upload_type}'. Choose 'gallery', 'camera', or 'location'."
            )

        # If using location-based upload, validate coordinates
        if self.upload_type == "location":
            self._validate_coordinates()

        # Validate image file (if provided)
        if value:
            self._validate_image(value)

        super().__init__(
            field_type="image",
            label=label,
            name=name,
            required=required,
            value=value,
            className=className,
        )

    def _validate_coordinates(self):
        """Validates that latitude and longitude are within correct ranges."""
        if self.latitude is None or self.longitude is None:
            raise ValueError(
                "Latitude and longitude are required for location-based upload."
            )

        if not (-90 <= self.latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees.")

        if not (-180 <= self.longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180 degrees.")

    def _validate_image(self, file_path):
        """Checks if the file is a valid image based on extension and size."""
        if not os.path.isfile(file_path):
            raise ValueError(f"File '{file_path}' does not exist.")

        # Validate file extension
        ext = os.path.splitext(file_path)[1][1:].lower()  # Extract file extension
        if ext not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"Invalid file format '{ext}'. Allowed formats: {', '.join(self.ALLOWED_EXTENSIONS)}"
            )

        # Validate file size
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB
        if file_size_mb > self.max_file_size:
            raise ValueError(
                f"File size exceeds the limit of {self.max_file_size}MB. Current size: {file_size_mb:.2f}MB."
            )

    def to_dict(self):
        """Returns the object data as a dictionary."""
        base_dict = super().to_dict()
        base_dict["upload_type"] = self.upload_type
        base_dict["latitude"] = self.latitude
        base_dict["longitude"] = self.longitude
        base_dict["max_file_size"] = self.max_file_size
        return base_dict

image_upload = ImageUploadClass(
        label="Upload Your Profile Picture",
        name="profile_pic",
        required=True,
        value="",  
        upload_type="gallery",
    )
    
print(image_upload.to_dict())