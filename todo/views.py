# imports django shortcuts, the render function is what is used to render html templates
from django.shortcuts import render
# imports Item class from models.py, 
# starting the library your pulling from with a "."
# indicates it it found locally
from .models import Item

# Create your views here.
# once a function to call the app has been created, 
# be sure to add the app to the INSTALLED_APPS[] variable inside settings.py, 
# in the main django_todo folder 
def get_todo_list(request):
    # in the imported class "Item", find objects, all of them
    items = Item.objects.all()
    # now the items variable has been established
    # the variable "context" is established as a dictionary
    # the key can be the name of whatever, but the value is the "items" variable
    context = {
        'items': items
    }
    # the context variable is passed into the the render return so now it is being
    # parsed into the todo_list.html template where the data can be accessed by a user
    return render(request, "todo/todo_list.html", context)
