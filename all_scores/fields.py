from django.db import models
from datetime import datetime, tzinfo
from time import strftime

class DateFromTimestampField(models.DateTimeField):
    def to_python(self, value):
        if isinstance(value, int):
            result = datetime.fromtimestamp(value)
            result.tzinfo = tzinfo.tzname("CET")
            return result 
        else:
            return models.DateTimeField.to_python(self, value)