from django.urls import path
from . import views
urlpatterns = [
    path("", views.home,name="home"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("allphotos/", views.allphoto, name="allphotos"),
    path("logout/",views.logout,name="logout")

]
