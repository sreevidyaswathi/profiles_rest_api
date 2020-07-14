from django.contrib import admin
from . import models
# Register your models here.
#we are registeringg our model to register with django admin
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
