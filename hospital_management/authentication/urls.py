from django.urls import path
from authentication.views import MyLoginView, logoutUser
urlpatterns = [
    path('', MyLoginView.as_view()),
    path('authenticate/', MyLoginView.as_view()),
    path('user/logout.do/', logoutUser, name='logout'),
]