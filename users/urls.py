from django.urls import path, include

from .custom_jwt_claims import CustomTokenObtainPairView

from users.views import ResetLoginAttemptsView, UpdateUserStatusView, DeleteUserView, UpdateUserView, UserView, NewUserView, AdminResetUserPasswordView, ResetUserPasswordView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('users/new', NewUserView.as_view(), name='new_user'),
    path('users/delete', DeleteUserView.as_view(), name='delete_user'),
    path('users/update-status', UpdateUserStatusView.as_view(), name='update_user_status'),
    path('users/update', UpdateUserView.as_view(), name='update_user'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/admin-reset-login-attempts', ResetLoginAttemptsView.as_view(), name="unblock"),
    path('users/admin-reset-password', AdminResetUserPasswordView.as_view(), name="admin_reset_password"),
    path('users/user-reset-password',ResetUserPasswordView.as_view(), name='reset_password'),
]