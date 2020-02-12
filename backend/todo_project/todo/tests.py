from django.test import TestCase
from .models import Todo

# Create your tests here.


class TestTodoModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="a todo", description='the todo body')

    def test_todo_title(self):
        todo = Todo.objects.get(id=1)
        expected_title = f'{todo.title}'
        self.assertEquals(expected_title, 'a todo')

    def test_todo_description(self):
        todo = Todo.objects.get(id=1)
        expected_description = f'{todo.description}'
        self.assertEquals(expected_description, 'the todo body')
