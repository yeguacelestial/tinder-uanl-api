# from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Group
from api.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
    class Meta:
        model = User
        fields = ['url', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']