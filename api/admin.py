from django.contrib import admin

from api import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'sex', 'age')

admin.site.register(models.User, UserAdmin)