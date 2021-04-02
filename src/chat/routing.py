# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # as_asgi() works same as .as_view()
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
