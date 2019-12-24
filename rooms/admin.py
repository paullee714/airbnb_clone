from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


# admin 안에 또 다른 admin
# TabularInline, StackInline 등이 있다
class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    inlines = (PhotoInline,)
    # fieldssets는 admin의 추가 화면들을 사용자가 꾸밀 수 있다.
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facility", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("hosts",)}),
    )

    # admin 에서 보여지는 컬럼
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "count_amenities",
        "count_photos",
        "check_in",
        "check_out",
        "instant_book",
        "total_rating",
    )

    # 정렬
    # ordering = ("name", "price", "bedrooms")

    # 우측 필터
    list_filter = (
        "instant_book",
        "hosts__superhost",
        "room_type",
        "amenities",
        "facility",
        "house_rules",
        "city",
        "country",
    )

    # 외부키를 잘 찾을 수 있게 도와줌
    # 선택 해야 하는 리스트가 클 경우 좋다.
    raw_id_fields = ("hosts",)

    search_fields = ("city", "hosts__username")

    filter_horizontal = ("amenities", "facility", "house_rules")

    # custom function
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    # custom label
    # count_amenities.short_description = "hello sexy"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src = "{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
