from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def username_validator(username):
    for char in username:
        if not (char.isalnum() or char in ["'", "_"]):
            raise ValidationError("Ensure this value contains only letters, numbers, apostrophe and underscore.")


def competition_title_validator(username):
    for char in username:
        if not (char.isalnum() or char in ["'", " "]):
            raise ValidationError("Ensure this value contains only letters, numbers, apostrophe and spaces.")


@deconstructible
class ValidateCloudinaryImage:
    def __init__(self, size):
        self.size = size

    def __call__(self, value):
        if '.' in str(value):
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'jfif']
            extension = value.name.split('.')[-1].lower()

            if extension not in valid_extensions:
                raise ValidationError('Unsupported file type. Allowed types are: jpg, jpeg, png, gif, webp, jfif')

            if value.size > self.size * 1024 * 1024:
                raise ValidationError('File size exceeds the limit of 500 KB.')
