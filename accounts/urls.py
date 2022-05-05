from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # path(
    #     "logout/",
    #     LogoutView.as_view(template_name="registration/logged_out.html"),
    #     name="logout",
    # ),
]

# path("logout/", auth_views.LogoutView.as_view(
#     template_name="accounts/registration/logout.html",
#     next_page=None
#   ), name="logout"),
