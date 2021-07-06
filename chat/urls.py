from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start_chat', views.start_chat, name="start_chat"),
    path('chats/<str:groupName>/<str:username>', views.chats, name="chats"),
    path('send_msg', views.send_msg, name="send_msg"),
]
