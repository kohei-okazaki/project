from django.contrib import admin
from .models import UserData, DailyUserWorkData

# Register your models here.
admin.site.register(UserData)
admin.site.register(DailyUserWorkData)
