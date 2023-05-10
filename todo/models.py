from django.db import models

# Create your models here.
# when a model is created her, 
# it is migrated into the database upon command. but it is created and modified here
# _________________________________________________
# the class name given becomes the name of the table.
# However, this will only do this if the models.Model parameter is given
# as this lifts the functionality of the "Model" class imported 
# from "models"at the top of the page from django.db
class Item(models.Model):
    # no need to create an id number field for this table, as django does this automatically
    # _________________________________________________
    # models.CharField() indicates that the field will only contain numbers and text
    # null=False: prevents a blank field being entered programmatically
    # blank=False: prevents the user from creating an entry without a name
    name = models.CharField(max_length=50, null=False, blank=False)
    # indicates that the field will contain a boolean value
    # default=False: automatically marks table item "not done" (in this instance)
    done = models.BooleanField(null=False, blank=False, default=False)

    # this string method is originally defined in the django libraries to give a
    # default value, however, it can be overriden by writing below like so, within the class
    # it uses the "self" argmument to target itself
    def __str__(self):
            # then it returns the value of the name variable establishes inside the class
            return self.name
