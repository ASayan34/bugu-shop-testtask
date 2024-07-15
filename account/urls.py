from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users', UserViewSet)  # Регистрация UserViewSet с именем 'users'

urlpatterns = [
    path('', include(router.urls)),  # Включение всех маршрутов из DefaultRouter
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Маршрут для получения токена
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Маршрут для обновления токена
]
