from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stamped Model
    Using This Class in EveryWhere
    to creaet,update timestamp
    """

    # 이 모델은 데이터베이스에 들어가며 안된다.
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
        # abstract Model :--> db에 Model이 들어가지 않는다.
