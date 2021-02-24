from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from user_session.serializers import UserSerializer, GroupSerializer

# dj rest auth
from allauth.socialaccount.providers.microsoft.views import MicrosoftGraphOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from config.settings import USER_SESSION_MICROSOFT_CALLBACK_URL

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MicrosoftLogin(SocialLoginView):
	"""
	API Endpoint that allows users to login with a Microsoft Account.
	"""
	adapter_class = MicrosoftGraphOAuth2Adapter
	callback_url = USER_SESSION_MICROSOFT_CALLBACK_URL
	client_class = OAuth2Client