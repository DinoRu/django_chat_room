"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.urls import re_path
from django.core.asgi import get_asgi_application

from app.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests'
    "http": django_asgi_app,
    # WebSocket handlers
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                re_path(r"^ws/chat/", ChatConsumer.as_asgi()),
            ]
        )
    )
})