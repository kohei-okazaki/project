from django.contrib import admin
from .models import UserData, DailyUserWorkData, CompanyMt, DivisionMt, OntimeMt

# Register your models here.
admin.site.register(UserData)
admin.site.register(DailyUserWorkData)
admin.site.register(CompanyMt)
admin.site.register(DivisionMt)
admin.site.register(OntimeMt)
