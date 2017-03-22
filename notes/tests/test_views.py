from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from notes.models import Note


class NoteTestViews(TestCase):
    def setUp(self):
        # create notes objects
        Note.objects.create(text="Buy pasta and tomatoes")
        Note.objects.create(text="Call to husband")
        Note.objects.create(text="Empty trash")

        self.client = Client()

        self.url = reverse('home')

    def test_notes_list(self):
        # make request to server to get home page
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertIn("Call to husband", response.content)

        self.assertEqual(len(response.context['notes']), 3)