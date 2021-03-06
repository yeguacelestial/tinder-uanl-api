from django.urls import include, path
from rest_framework import routers
from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'groups', views.GroupViewSet, basename='group')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # DRF
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Django allauth
    path('accounts/', include('allauth.urls')),

    # Dj rest auth
    path('dj_rest_auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/microsoft/', views.MicrosoftLogin.as_view(), name='ms_login'),
]