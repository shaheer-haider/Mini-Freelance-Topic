from typing import Any
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from users.models import CustomUser as User
from django.contrib.auth.admin import UserAdmin


from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    def __init__(self, model, admin_site):
        self.list_display = list(self.list_display)
        self.list_display.append("image")
        super().__init__(model, admin_site)

admin.site.register(User, CustomUserAdmin)
