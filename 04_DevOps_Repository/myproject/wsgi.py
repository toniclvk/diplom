"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.contrib.auth.models import User
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

users = User.objects.all()
if not users:
    User.objects.create_superuser(username="{{var_username_wsgi}}", email="toniclvk@example.com",
                                  password="{{var_password_wsgi}}", is_active=True, is_staff=True)

