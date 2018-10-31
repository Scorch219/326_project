from django.contrib import admin

# Register your models here.
from umarket.models import UserAccount, Product

admin.site.register(UserAccount)
admin.site.register(Product)
