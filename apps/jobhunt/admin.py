from django.contrib import admin

from apps.jobhunt.models import Vacancy, Resume, Company

admin.site.register(Vacancy)
admin.site.register(Resume)
admin.site.register(Company)
