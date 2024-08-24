from django.contrib import admin

from User.models import User, Role

# Register your models here.

admin.site.register(Role)
admin.site.register(User)