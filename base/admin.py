from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

from .models import Room, Topic, Message, User

admin.site.register(User) #admin
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
