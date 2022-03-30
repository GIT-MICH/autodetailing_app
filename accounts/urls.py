from django.urls import path
from accounts.views import LoginView, LogoutView, RegisterView, UserPermissionUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('set_permission/<int:user_id>/', UserPermissionUpdateView.as_view(), name='set-permission'),
]



#     path('set_permission/<int:user_id>/', UserPermissionUpdateView.as_view(), name='set_permission'),