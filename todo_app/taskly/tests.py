from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Todo
from datetime import timedelta

class TodoTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.todo = Todo.objects.create(
            title="Test Task",
            details="Test task details",
            due_date=timezone.now() + timedelta(days=1)
        )

    def test_todo_creation(self):
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(self.todo.title, "Test Task")
        self.assertFalse(self.todo.is_completed)

    def test_invalid_due_date(self):
        past_date = timezone.now() - timedelta(days=1)
        todo = Todo(
            title="Past Due",
            due_date=past_date
        )
        with self.assertRaises(Exception):  # ValidationError
            todo.full_clean()  # Triggers the `clean()` method

    def test_index_view_status_code(self):
        response = self.client.get(reverse('taskly'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_remove_task_view(self):
        response = self.client.get(reverse('remove', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(Todo.objects.count(), 0)
