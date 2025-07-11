from django.urls import path
from . import views

app_name = "messenger"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("send/", views.send_message, name="send_message"),
]
