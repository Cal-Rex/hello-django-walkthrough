# imports django shortcuts, the render function is what is used to render html templates
from django.shortcuts import render, redirect, get_object_or_404
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


# updating an item
def edit_item(request, item_id):
    # the variable searches for an object in the first parameter (Item)
    # which has been treated like an object thanks to the python method
    # "get_object_or_404"
    # then takes the second parameter as that object's id Key's value
    # and that objects value is given by the Item that is printed on the
    # html template, which is parsed to this method via the URL
    # stated with angular brackets in urls.py
    item = get_object_or_404(Item, id=item_id)
    # for the edit form, updating method is almost identical to the
    # method to adding items.
    # the difference here, is that an "instance" parameter is added to
    # the "ItemForm" handler inside the "form" variable
    # which has now targeted that specific database entry to update.
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # generates the same form as add_item function
    # EXCEPT - the instance parametr loads all of the details
    # into the fields of the form by calling on the "item"
    # variable established above
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, "todo/edit_item.html", context)

    
def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')