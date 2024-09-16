from django.urls import path
from app.views import login
urlpatterns = [
    path('login/', login, name='login')
]

