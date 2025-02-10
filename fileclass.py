from base import BaseClass

class FileClass(BaseClass):

    def __init__(
        self,
        label,
        name,
        required=False,
        value=None,
        accept_types=None,
        className="form-control-file",
    ):
        super().__init__(
            field_type="file",
            label=label,
            name=name,
            required=required,
            value=value,
            className=className,
        )
        self.accept_types = (
            accept_types if accept_types else []
        )  # List of accepted file types

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["accept_types"] = self.accept_types  # Include the accepted file types
        return base_dict
    
    

    def validate_file(self, file_name):
        """
        Validates the file based on the accepted types.
        It checks if the file's extension matches one of the accepted types.
        """
        if not self.accept_types:
            return True  # No restrictions, any file type is allowed

        file_extension = file_name.split(".")[-1].lower()
        # Get the file extension (lowercased)
        if file_extension in self.accept_types:
            return True
        else:
            return False
        
# if __name__ == "__main__":
#     # Step 1: Create an instance of FileUploadClass
#     file_upload_field = FileClass(
#         label="Upload your resume",
#         name="resume",
#         required=True,
#         accept_types=["pdf", "docx"],  # Only PDF and DOCX files are allowed
#     )

#     # Step 2: Test the `to_dict()` method
#     print("Dictionary Representation of the File Upload Field:")
#     print(file_upload_field.to_dict())

#     # Step 3: Test file validation with different file types
#     test_files = ["resume.pdf", "image.jpg", "report.docx", "presentation.pptx"]

#     print("\nFile Validation Results:")
#     for file_name in test_files:
#         is_valid = file_upload_field.validate_file(file_name)
#         print(f"Is the file '{file_name}' valid? {is_valid}")
# 4
