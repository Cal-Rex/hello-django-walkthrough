from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestItemForm(TestCase):

    def test_item_name_req(self):
        # when the test creates this variable, 
        # the variable runs an instance 
        # of the process inside itself
        form = ItemForm({'name': ''})
        # assertFalse checks the form variable above, in the instance of
        # the "is_valid" method being run on it, asserting that it should be false
        # should the data not return false, an F would be raised on the test 
        self.assertFalse(form.is_valid())
        # When the form is invalid it should also send back a dictionary of fields on which
        # there were errors and the Associated error messages
        # because of this, we can refine what caused the error by using "assertIn"
        # to detect wether or not there is a 'name' key in the dictionary of the compiled
        # dictionary provided from the error
        self.assertIn('name', form.errors.keys())
        # assertEqual tests the value here of the produced error message for the value
        # of the name key in the instances form, which is currently blank.
        # because of this, the following string shouldbe produced by the system
        # so it can be checked to see if it shows up.
        # p.s: the string needs to match exactly
        # p.s.p.s: list notation is used for the name key because python will return a list
        #          of errors for each form field
        self.assertEqual(form.errors['name'][0], 'This field is required.')


    def test_done_not_req(self):
        form = ItemForm({'name': 'test item'})
        # asserts within the variable instance that the form SHOULD be valid 
        # with the given parameters above
        self.assertTrue(form.is_valid())


    def test_fields_meta_confirmed(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])

