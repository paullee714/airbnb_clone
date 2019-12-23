from django.db import models
from core import models as core_models
from django_countries.fields import CountryField

# from users import models as user_models
# --> Model을 import 해서 직접 사용 할 수 있지만
## 모델의 이름을 String으로 해서 처리하면 import 가 필요 없다.


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ RoomType """

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):
    """ Amenity """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Facility """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """House Rule"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """ Photo Model"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    ## 모델의 이름을 String으로 해서 처리하면 import 가 필요 없다.
    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)  # Required Dosent need null,blank
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # host는 다른 모델과 이어주어야 함
    hosts = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facility = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
