from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ MessageAdmin"""

    pass


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """ ConversationAdmin"""

    pass
