from django.contrib import admin
from .models import Item

# Register your models here.
# allows admins to register the model called Item in models.py
admin.site.register(Item)