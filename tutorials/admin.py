from django.contrib import admin

# Register your models here.
from .models import Tutorial, Topic


admin.site.register(Tutorial)
admin.site.register(Topic)