from django.contrib import admin
from basic_app.models import School,Student,UserProfileInfo
# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(UserProfileInfo)
