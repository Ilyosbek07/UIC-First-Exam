from django.contrib import admin

from apps.avto.models import Type, Brand, Announcement

admin.site.register(Type)
admin.site.register(Brand)
admin.site.register(Announcement)
