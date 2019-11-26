from django.urls import path
from . import views

app_name='server'

urlpatterns = [
    # /meeting/create/ endpoint will create meeting
    path('create/', views.Meeting.as_view(), name="create_meeting")
]