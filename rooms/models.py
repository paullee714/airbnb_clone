from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from django.urls import reverse

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
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)
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
    hosts = models.ForeignKey(
        # manage.py shell에서 받아올 _set 과 관련된 이름 : related_name
        "users.User",
        related_name="rooms",
        on_delete=models.CASCADE,
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    # super()를 사용해, 기존 save 메서드에 추가적으로 나의 코드를 실행
    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    # absolute url
    # absolute url이 적용되면 해당 url로 이동 됨
    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    # 전체 리뷰의 평균
    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

    # 방 사진 가져오기
    def first_photo(self):
        (photo,) = self.photos.all()[:1]
        return photo.file.url
