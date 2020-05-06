from django.contrib import admin
from basicapp.models import UserProfileInfo,members,ActivityPeriod

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(members)
admin.site.register(ActivityPeriod)
