from django.contrib import admin

# Register your models here.
from umarket.models import Profile, Product

admin.site.register(Profile)
admin.site.register(Product)
