from django.contrib import admin

from .models import flight,airport,passengers
# Register your models here.

admin.site.register(flight)
admin.site.register(airport)
admin.site.register(passengers)

