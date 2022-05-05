from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
  path("signup/", SignUpView.as_view(), name="signup"),
  path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

# path("logout/", auth_views.LogoutView.as_view(
#     template_name="accounts/registration/logout.html",
#     next_page=None
#   ), name="logout"),