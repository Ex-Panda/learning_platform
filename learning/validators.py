from rest_framework.serializers import ValidationError


class TitleValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if tmp_value is not None and "https" in tmp_value and 'youtube.com' not in tmp_value:
            raise ValidationError('Вы можете ссылаться только на youtube.com')
