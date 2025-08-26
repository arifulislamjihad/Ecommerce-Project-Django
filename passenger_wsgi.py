import sys, os

# Project path যোগ করুন
sys.path.insert(0, "/home/arifunifiedit/shop.aboronifashion.xyz")

# Settings ফাইল সেট করুন
os.environ['DJANGO_SETTINGS_MODULE'] = 'e_shop.settings'

# Django WSGI application load করুন
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
