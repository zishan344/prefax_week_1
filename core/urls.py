from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from core.views import NoteViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet, )

urlpatterns = [
    path('login/',obtain_auth_token),
    # path('',include('router.urls'))
    path('', include(router.urls)),
]
