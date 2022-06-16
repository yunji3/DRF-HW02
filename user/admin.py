from django.contrib import admin
from user.models import User as UserModel
from user.models import UserProfile as UserProfilModel
from user.models import Hobby as HobbyModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(UserProfilModel)
admin.site.register(HobbyModel)
