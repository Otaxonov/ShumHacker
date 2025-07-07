from django.core.exceptions import ValidationError


def title_starts_with_a(value):
    if not value.startswith('a'):
        raise ValidationError('Title Must Start with a')
    return value
