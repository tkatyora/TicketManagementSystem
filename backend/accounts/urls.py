from django.urls import path, include
from .views import (LoginAPIView,
                    UserManagementViewSet,
                     ActivateAccountAPIView,
                     LogoutAPIView
                    )
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'stsusers', UserManagementViewSet)


urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('', include(router.urls)),
    path('activate/', ActivateAccountAPIView.as_view()),
]
