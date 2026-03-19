"""
ASGI config for due_book project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'due_book.settings')

application = get_asgi_application()
