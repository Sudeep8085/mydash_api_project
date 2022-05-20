from django.urls import path
from . import views
urlpatterns = [
    path("register/",views.user_register),
    path("login/",views.user_Login),
    path("messages/",views.MessageView.as_view()),
]
