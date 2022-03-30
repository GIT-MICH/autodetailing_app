from django.urls import path
from accounts.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]


#     path('registration/', AddUser.as_view(), name='registration'),
#     path('set_permission/<int:user_id>/', UserPermissionUpdateView.as_view(), name='set_permission'),