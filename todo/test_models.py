from django.test import TestCase
# import the models.py Item class so it can be tested directly here
from .models import Item

# Create your tests here.
class TestModels(TestCase):

    # this test checks to make sure that the
    # default value of any entry - if it isnt
    # assigned "done" it will be allocated
    # a False value
    def test_false_is_default(self):
        # first, create the item on an instanced database simulation
        item = Item.objects.create(name='Test Todo Item')
        # check to see if it's been allocated a false value
        # as we did not specify a boolean value in the above parameters
        self.assertFalse(item.done)

    # checks to see if the name value of the name field is a string value
    def test_string_is_name(self):
        item = Item.objects.create(name='test Todo Item')
        # checks to see if the value of "item" is a string
        # and that it matches the original input
        self.assertEqual(str(item), 'Test Todo Item')
       
    