from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register the User model so it appears in the admin panel
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # This adds the 'role' field to the user editing screen
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff')