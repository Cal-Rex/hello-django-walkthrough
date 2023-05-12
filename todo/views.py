# imports django shortcuts, the render function is what is used to render html templates
from django.shortcuts import render, redirect
# imports Item class from models.py, 
# starting the library your pulling from with a "."
# indicates it it found locally
from .models import Item
# allow importing of the ItemForm class from forms.py
# for use as the form element on this page
from .forms import ItemForm

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

# for add item page
def add_item(request):
    # if statement used for when form is submitted and page reloads.
    # when the form is POSTed, this following function commands run
    if request.method == "POST":
        #===========================
        # METHOD FOR USING HTML CREATED FORM
        # ___________________________________
        # variable names used here match the variable names clarified in models.py
        # under the class "Item"
        # ___________________________________
        # pulls the value of the form field with the name attribute "item_name"
        # name = request.POST.get('item_name')
        # pulls the boolean value of the form field with the name "done"
        # done = 'done' in request.POST
        # next command creates an object out of the form data, 
        # and marries the values up with the variable names listed in the class
        # Item.objects.create(name=name, done=done)
        # return redirect('get_todo_list')
        # ==========================
        # METHOD FOR USING PYTHON/DJANGO CREATED FORM
        # ___________________________________________
        # the form variable below corresponds to the instance 
        # where ItemForm imported from django is submitted
        form = ItemForm(request.POST)
        # if statament checks if all value is the form are valid
        if form.is_valid():
            # then saves the form
            form.save()
            # then redirects to homepage
            return redirect('get_todo_list')
        # ===========================
    # takes the imported form and applies it to a variable
    form = ItemForm()
    # when an imported item is established as a variable
    # it's context must be established:
    context = {
        'form': form
    }
    return render(request, "todo/add_item.html", context)