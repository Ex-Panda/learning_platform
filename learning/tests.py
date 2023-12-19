from rest_framework import status
from rest_framework.test import APITestCase

from learning.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create(
            email='frausonya131@gmail.com',
            first_name='Admin',
            last_name='Mailing',
            is_active=True
        )

        user.set_password('123qwe456rty')
        user.save()
        response = self.client.post(
            '/token/',
            data={
                    "email": "frausonya131@gmail.com",
                    "password": "123qwe456rty"
                    }
        )
        self.token = response.json()["access"]

        self.user = user

    def test_create_lesson(self):
        """Тестирование создания урока"""
        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        course = Course.objects.create(name_course='Первый курс', description_course='Самый первый тестовый')
        data = {
            'name_lesson': 'Test lesson',
            'description_lesson': 'test test',
            'url_video': 'http/youtube.com',
            'course': course.id
        }
        response = self.client.post(
            '/lesson/create',
            data=data,
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': response.json()['id'], 'name_lesson': 'Test lesson', 'description_lesson': 'test test', 'preview_lesson': None,
             'url_video': 'http/youtube.com', 'course': course.id, 'user': response.json()['user']}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        """ Тестирование вывода списка уроков """
        course = Course.objects.create(name_course='Первый курс', description_course='Самый первый тестовый')
        lesson = Lesson.objects.create(
            name_lesson='Test lesson',
            description_lesson='test test',
            url_video='http/youtube.com',
            course=course,
            user=self.user
        )
        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.get(
            '/lesson',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': lesson.id, 'name_lesson': 'Test lesson', 'description_lesson': 'test test', 'preview_lesson': None,
             'url_video': 'http/youtube.com', 'course': course.id, 'user': self.user.id}]
        )

    def test_retrieve_lesson(self):
        """Тестирование вывода одного урока"""
        course = Course.objects.create(name_course='Первый курс', description_course='Самый первый тестовый')
        lesson = Lesson.objects.create(
            name_lesson='Test lesson',
            description_lesson='test test',
            url_video='http/youtube.com',
            course=course,
            user=self.user
        )
        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.get(
            f'/lesson/{lesson.id}',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': lesson.id, 'name_lesson': 'Test lesson', 'description_lesson': 'test test',
             'preview_lesson': None,
             'url_video': 'http/youtube.com', 'course': course.id, 'user': self.user.id}
        )

    def test_update_lesson(self):
        """Тестирование редактирования урока"""
        course = Course.objects.create(name_course='Первый курс', description_course='Самый первый тестовый')
        lesson = Lesson.objects.create(
            name_lesson='Test lesson',
            description_lesson='test test',
            url_video='https/youtube.com',
            course=course,
            user=self.user
        )
        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        data = {
            'name_lesson': 'Test lesson update'
        }

        response = self.client.patch(
            f'/lesson/update/{lesson.id}',
            data=data,
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['name_lesson'],
            'Test lesson update'
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        course = Course.objects.create(name_course='Первый курс', description_course='Самый первый тестовый')
        lesson = Lesson.objects.create(
            name_lesson='Test lesson',
            description_lesson='test test',
            url_video='http/youtube.com',
            course=course,
            user=self.user
        )
        heard = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.client.delete(
            f'/lesson/delete/{lesson.id}',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create(
            email='frausonya131@gmail.com',
            first_name='Admin',
            last_name='Mailing',
            is_active=True
        )

        user.set_password('123qwe456rty')
        user.save()
        response = self.client.post(
            '/token/',
            data={
                "email": "frausonya131@gmail.com",
                "password": "123qwe456rty"
            }
        )
        self.token = response.json()["access"]

        self.user = user

    def test_create_subscription(self):
        """Тестирование создания подписки"""
        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        course = Course.objects.create(name_course='Первый курс', description_course='Самый первый тестовый')
        data = {
            'course_subscription': course.id,
        }
        response = self.client.post(
            '/subscription/create',
            data=data,
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_subscription(self):
        """Тестирование удаления подписки"""
        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        course = Course.objects.create(name_course='Первый курс', description_course='Самый первый тестовый')
        subscription = Subscription.objects.create(
            user=self.user,
            course_subscription=course
        )
        response = self.client.delete(
            f'/subscription/delete/{subscription.id}',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
