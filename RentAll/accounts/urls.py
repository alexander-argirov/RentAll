from django.contrib import staticfiles
from django.urls import path


from RentAll.accounts.views import SignInUserView, RegisterUserView, signout_user, ProfileDetailsView, \
    ProfileUpdateView, ProfileDeleteView, PasswordChange

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('signin/', SignInUserView.as_view(), name='signin user'),
    path('signout/', signout_user, name="signout user"),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='detail profile'),
    path('edit/<int:pk>/', ProfileUpdateView.as_view(), name='edit profile'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='delete profile'),
    path('password_change/<int:pk>/', PasswordChange.as_view(), name='password change view'),
]

