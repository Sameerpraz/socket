"""
ASGI config for Djangosocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
# import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import src.chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Djangosocket.settings')
# django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
            URLRouter(
                src.chat.routing.websocket_urlpatterns
            )
        ),
    # Just HTTP for now. (We can add other protocols later.)
})