from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ CUSTOM USER ADMIN """

    # list_display = (
    #     "username",
    #     "email",
    #     "gender",
    #     "language",
    #     "currency",
    #     "superhost",
    # )
    # list_filter = ("superhost", "language", "currency")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "birthdate",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
