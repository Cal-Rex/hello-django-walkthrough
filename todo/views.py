# imports django shortcuts, the render function is what is used to render html templates
from django.shortcuts import render


# Create your views here.
# once a function to call the app has been created, 
# be sure to add the app to the INSTALLED_APPS[] variable inside settings.py, 
in the main django_todo folder 
def get_todo_list(request):
    return render(request, "todo/todo_list.html")
