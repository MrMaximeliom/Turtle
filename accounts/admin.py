from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile
# Register your models here.

class AccountAdmin(UserAdmin):
    # customizing users list
    list_display = ('email','username','date_joined','last_login','is_admin','is_staff','is_teacher','is_student')
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User,AccountAdmin)
admin.site.register(Profile)