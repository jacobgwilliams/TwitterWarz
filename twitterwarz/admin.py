from django.contrib import admin

# Register your models here.
from .models import User
from .models import Tweet
from .models import Battle

admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Battle)
