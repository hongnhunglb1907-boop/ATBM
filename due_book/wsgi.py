"""
WSGI config for due_book project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'due_book.settings')

application = get_wsgi_application()
