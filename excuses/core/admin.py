from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site

from excuses.core.models import Excuse


admin.site.register(Excuse)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Site)

