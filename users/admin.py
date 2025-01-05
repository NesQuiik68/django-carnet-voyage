
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'isLoggedIn')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('isLoggedIn',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('isLoggedIn',)}),
    )

admin.site.register(User, CustomUserAdmin)