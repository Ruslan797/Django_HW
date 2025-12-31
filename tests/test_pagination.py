# from rest_framework.test import APITestCase
# from rest_framework.reverse import reverse
# from taskmanager.models import Task
#
# class PaginationTestCase(APITestCase):
#     def setUp(self):
#         for i in range(10):
#             Task.objects.create(name=f'Task {i}')
#
#     def test_pagination_page_size(self):
#         url = reverse('task-list-create')
#         response = self.client.get(url)
#         self.assertEqual(len(response.data['results']), 6)  # Проверка, что на странице 6 объектов
#
#     def test_cursor_pagination(self):
#         url = reverse('task-list-create')
#         response = self.client.get(url)
#         self.assertIn('next', response.data)  # Проверка наличия ссылки на следующую страницу


from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from taskmanager.models import Task
from django.utils import timezone
from datetime import timedelta


class PaginationTestCase(APITestCase):
    def setUp(self):
        for i in range(15):
            Task.objects.create(
                title=f'Task {i}',
                description="Test description",
                deadline=timezone.now() + timedelta(days=7)
            )

        # for i in range(10):
        #     Task.objects.create(title=f'Task {i}')

    def test_page_size_is_6(self):
        url = reverse('task-list-create')
        response = self.client.get(url)

        # На странице должно быть 6 объектов
        self.assertEqual(len(response.data['results']), 6)

    def test_cursor_pagination_structure(self):
        url = reverse('task-list-create')
        response = self.client.get(url)

        # Проверяем структуру ответа
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertIn('results', response.data)

    def test_next_page_exists(self):
        url = reverse('task-list-create')
        response = self.client.get(url)

        # Должна быть ссылка на следующую страницу
        self.assertIsNotNone(response.data['next'])

    def test_second_page_has_previous(self):
        url = reverse('task-list-create')

        # Получаем ссылку на вторую страницу
        response = self.client.get(url)
        next_url = response.data['next']

        response_page2 = self.client.get(next_url)

        # Вторая страница должна иметь previous
        self.assertIsNotNone(response_page2.data['previous'])

        # И должна содержать 4 объекта (10 - 6)
        self.assertEqual(len(response_page2.data['results']), 4)

