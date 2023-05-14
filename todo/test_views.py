from django.test import TestCase
# import the "Item" class from models.py so that you can
# run a test server without having to run it on the actual database. but it should yield
# the same results
from .models import Item


# Create your tests here.
class TestViews(TestCase):
   
    def test_todo_pg(self):
        # variable creates an instance where it attampts 
        # to load the page with the url "/" (blank) by using the
        # Django built-in httpResponse testing mechanism called
        # client.get
        response = self.client.get('/')
        # assertEqual checks to see here that the status code (status_code)
        # of the instanced page loaded is "200", AKA
        # a succeffuly get request/connection
        self.assertEqual(response.status_code, 200)
        # checks to make sure the following template is used for this page
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    # same as above, but with the add template
    def test_add_item_pg(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_edit_item_pg(self):
        # because Item is imported from models.py at the top of the page
        # an instance of the database can be created locally inside the "item"
        # variable.
        item = Item.objects.create(name='Test Todo Item')
        # because of this, we can run a generic test on
        # an item with an id via the url if using a python f-string
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # client action, but this time it will post the value of the second parameter
        # to the instanced database
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # confirms that the page redirects on a succesful post
        self.assertRedirects(response, '/')
    
    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        # created item above is deleted
        response = self.client.get(f'/delete/{item.id}')
        # confirms redirect
        self.assertRedirects(response, '/')
        # variable then searches the database for entries and filter them
        # by their id. but there should be no items as this instanced database
        # only had an item originally created above, and then deleted by
        # the next line of code
        existing_items = Item.objects.filter(id=item.id)
        # the test below then confirms that the number of items in that returned
        # list is zero, as there should be no entries after a successful
        # deletion
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # create an item with the True boolean
        item = Item.objects.create(name='Test Todo Item', done=True)
        # create a response variable that runs the toggle function
        response = self.client.get(f'/toggle/{item.id}')
        # use the response variable as a parameter
        self.assertRedirects(response, '/')
        # apply the Item to a variable so we can check it
        updated_item = Item.objects.get(id=item.id)
        # check to see if it's value has changed from True to False
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')