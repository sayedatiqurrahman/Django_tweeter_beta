"""
WSGI config for TweeterBeta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TweeterBeta.settings')

# application = get_wsgi_application()


# app = application


import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TweeterBeta.settings")

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception as e:
    # This helps debugging on Vercel
    import sys
    print("WSGI Error:", e, file=sys.stderr)
    application = None


app = application