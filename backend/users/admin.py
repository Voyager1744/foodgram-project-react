from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',
                    'username',
                    'first_name',
                    'last_name',
                    'is_superuser',
                    'is_active',
                    )
    search_fields = ('email', 'username', 'first_name', 'last_name',)
    ordering = ('id', 'email', 'username',)
