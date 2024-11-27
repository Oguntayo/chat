import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from app1.routing import websocket_urlpatterns  # Import the WebSocket routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'registration.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Include WebSocket URL routing here
        )
    ),
})
