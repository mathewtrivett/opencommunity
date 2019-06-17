from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','is_staff','is_active','last_login',)
    search_fields = ('username','email',)

admin.site.register(User,UserAdmin)
