from rest_framework.serializers import ValidationError


class TitleValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if tmp_value is not None and "https" in tmp_value and 'youtube.com' not in tmp_value:
            raise ValidationError('Вы можете ссылаться только на youtube.com')


class PayValidator:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        pay_value1 = dict(value).get(self.field1)
        pay_value2 = dict(value).get(self.field2)

        if (pay_value1 is None and pay_value2 is None) or (pay_value1 is not None and pay_value2 is not None):
            raise ValidationError('Вы можете оплатить только одну позицию')
