from django.contrib import admin
from kintai.models import BusinessCalendarMt, UserData, DailyUserWorkData, CompanyMt, DivisionMt, OntimeMt, UserDataHist

# Register your models here.
admin.site.register(UserData)
admin.site.register(UserDataHist)
admin.site.register(DailyUserWorkData)
admin.site.register(CompanyMt)
admin.site.register(DivisionMt)
admin.site.register(OntimeMt)
admin.site.register(BusinessCalendarMt)
