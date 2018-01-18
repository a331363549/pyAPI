from django.contrib import admin

# Register your models here.
from test_user import models


admin.site.register(models.UserInfo)
admin.site.register(models.TestData)
