import io
import os

from django.urls import reverse
from django.test import TestCase

from PIL import Image
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APITestCase

from api.models import User


class UserSessionTest(APITestCase):

    def setUp(self):
        """
            Create normal user instance.
        """
        self.normal_user = User.objects.create(
            email="pablo.barreragzz@uanl.edu.mx",
            first_name="Pablo",
            last_name="Barrera",
        )
        self.normal_user.set_password('test12345')
        self.normal_user.save()
        self.normal_token, created = Token.objects.get_or_create(user=self.normal_user)

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