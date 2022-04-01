from django.urls import path
from accounts.views import LoginView, LogoutView, RegisterView, UserPermissionUpdateView, AllAccountsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('all/set_permission/<int:user_id>/', UserPermissionUpdateView.as_view(), name='set-permission'),
    path('all/', AllAccountsView.as_view(), name='all-users'),

]



#     path('set_permission/<int:user_id>/', UserPermissionUpdateView.as_view(), name='set_permission'),