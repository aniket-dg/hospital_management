from django.urls import path
from authentication.views import MyLoginView
urlpatterns = [
    path('', MyLoginView.as_view()),
    path('authenticate/', MyLoginView.as_view()),
]