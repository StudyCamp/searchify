from django.urls import path

from . import views

app_name = "searchifyApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("share/", views.create, name="share"),
    path("search/", views.search, name="search"),
    path("searchTag/", views.searchTag, name="searchTag"),
    path("searchContent/", views.searchContent, name="searchContent"),
    path("result/<str:tag>/", views.result, name="result"),
    path("contentResult/<str:content>/", views.contentResult, name="contentResult"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("find", views.find, name="find"),
    path("userlist/<str:username>/", views.userlist, name="userlist"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register")

]