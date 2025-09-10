from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskViewsTest(TestCase):
    def test_task_list_view_renders(self):
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add")  # confirm form rendered

    def test_add_task(self):
        response = self.client.post(reverse("add_task"), {"title": "Test task"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(title="Test task").exists())


class TaskModelTest(TestCase):
    def test_string_representation(self):
        task = Task(title="Do laundry")
        self.assertEqual(str(task), "Do laundry")
