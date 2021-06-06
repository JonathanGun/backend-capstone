import logging

from django.contrib import admin
from django.core.cache import cache
from djangoql.admin import DjangoQLSearchMixin

from api.models import *

logger = logging.getLogger()


class BaseAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    ordering = ('id',)
    list_per_page = 10
    list_display = []
    readonly_fields = ['created_at', 'updated_at']


@admin.register(User)
class UserAdmin(BaseAdmin):
    ordering = ('google_id',)
    list_display = [f.name for f in User._meta.fields]
    readonly_fields = []
    can_delete = False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Travel)
class TravelAdmin(BaseAdmin):
    list_display = [f.name for f in Travel._meta.fields]
    readonly_fields = []
    can_delete = False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Picture)
class TravelAdmin(BaseAdmin):
    list_display = [f.name for f in Picture._meta.fields]
    readonly_fields = []
    can_delete = False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(TravelLog)
class TravelLogAdmin(BaseAdmin):
    list_display = [f.name for f in TravelLog._meta.fields]
    readonly_fields = []
    can_delete = False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False