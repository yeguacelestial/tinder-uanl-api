import io
import os

from django.test import TestCase
from django.urls import reverse

from PIL import Image

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APITestCase

from api.models import User


class UserHandlingTest(APITestCase):

    def setUp(self):
        """
        Create normal user instance.
        """
        self.normal_user = User.objects.create(
            email="pablo.barreragzz@uanl.edu.mx",
            first_name="Pablo",
            last_name="Barrera",
            is_staff=True
        )
        self.normal_user.set_password('test12345')
        self.normal_user.save()
        self.normal_token, created = Token.objects.get_or_create(user=self.normal_user)

    def test_created_user_exists(self):
        """
        Test if user created on setup exists.
        """

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.normal_token.key)

        response = self.client.get(reverse('api:user-list'))
        results = response.json()

        dummy_user_email = results[0]['email']

        self.assertEqual(dummy_user_email, 'pablo.barreragzz@uanl.edu.mx')

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')

        file.name = 'test.png'
        file.seek(0)
        return file
    
    def _test_upload_photo(self):
        """
            Test if we can post a photo.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.normal_token.key}')

        photo_file = self.generate_photo_file()

        data = {
            'profile_pictures': photo_file,
        }

        response = self.client.post('api/v1/user-session/users/2/', data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
