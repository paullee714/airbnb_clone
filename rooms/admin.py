from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

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

    pass
