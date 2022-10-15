from django.test import TestCase
from .forms import EventForm
# Create your tests here.

class CheckEventModel(TestCase):
    def test_create_event_form(self):
        form = EventForm(data={
            'name': 'test_name',
            'event_date': '2022-07-02 10:23:11'
        })
        self.assertTrue(form.is_valid())





