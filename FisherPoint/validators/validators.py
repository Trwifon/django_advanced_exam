from django.core.exceptions import ValidationError

def username_validator(username):
    for char in username:
        if not (char.isalnum() or char == '_'):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def competition_title_validator(username):
    for char in username:
        if not (char.isalnum() or char == ' '):
            raise ValidationError("Ensure this value contains only letters, numbers, and spaces.")