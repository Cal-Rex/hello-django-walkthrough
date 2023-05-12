# imports the forms library from django
from django import forms
# imports the Item class from the local models.py file
from .models import Item

# class calls on the Modelform class inside the forms library from django
class ItemForm(forms.ModelForm):
    # class meta used here to establish the metadata of the form element
    class Meta:
        # the model is the imported Item model from models.py
        model = Item
        # then the fields are listed as a python list of strings 
        # that match the variable names
        fields = ['name', 'done']