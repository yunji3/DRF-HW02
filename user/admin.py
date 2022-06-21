from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib import admin
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfileModel
    filter_horizontal=['hobby']

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', )
    list_filter = ('username',)
    search_fields = ('username', 'email', )

    fieldsets = (
        ('info', {'fields':('username', 'password', 'email', 'fullname', 'join_date',)}),
        ('Permissions', {'fields':('is_admin', 'is_active',)}),)
    inlines = (
        UserProfileInline,
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email', 'fullname', 'password', 'password2')
        }),
    )
    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date',)
        else:
            return ('join_date',)


admin.site.register(UserModel, UserAdmin)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)
