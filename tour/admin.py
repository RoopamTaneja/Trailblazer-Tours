from django.contrib import admin

from .models import Tour
from .models import Contact
from .models import Profile

admin.site.register(Tour)
admin.site.register(Contact)
admin.site.register(Profile)
