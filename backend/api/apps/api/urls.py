from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views.silos_view import SilosViewSet
from .views.zones_view import ZonesViewSet
from .views.liquids_view import LiquidsViewSet
from .views.actions_view import ActionsViewSet


router = routers.DefaultRouter()
router.register('liquids', LiquidsViewSet)
router.register('zones', ZonesViewSet)
router.register('silos', SilosViewSet)
router.register('actions', ActionsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token)
]
