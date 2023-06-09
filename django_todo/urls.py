"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# any new templates made need to be imported here like a library!
# ________________________
# this can be done with dot notation in the "from" part of the import:
# from todo.views import get_todo_list, add_item, edit_item
# or you can import the whole views file if you have a lot of 
# paths
from todo import views
# if the method above is used, all paths need to use the dot notation
# for their function name. see:
# path('', views.get_todo_list, name='get_todo_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    # add new pages' path here, you need to first specify what the path on the link is
    # then you need to call the function written in views.py
    # then name the path appropriately
    path('', views.get_todo_list, name='get_todo_list'),
    path('add', views.add_item, name='add'),
    # angular bracket tag is important here:
    # It is the mechanism by which the item ID 
    # makes its way from links or forms in our html templates.
    # Through the URL and into the views.py which expects it as a parameter.
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete')
]
