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
from todo.views import get_todo_list, add_item, edit_item

urlpatterns = [
    path('admin/', admin.site.urls),
    # add new pages' path here, you need to first specify what the path on the link is
    # then you need to call the function written in views.py
    # then name the path appropriately
    path('', get_todo_list, name='get_todo_list'),
    path('add', add_item, name='add'),
    # angular bracket tag is important here:
    # It is the mechanism by which the item ID 
    # makes its way from links or forms in our html templates.
    # Through the URL and into the views.py which expects it as a parameter.
    path('edit/<item_id>', edit_item, name='edit')
]
