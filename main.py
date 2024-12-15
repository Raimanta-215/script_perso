import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line

def configure_django():
    if not settings.configured:
        settings.configure(
            SECRET_KEY='votre_cle_secrete_ici',
            DEBUG=True,
            INSTALLED_APPS=[
                'django.contrib.contenttypes',
                'django.contrib.auth',
                # Ajoutez vos applications ici
            ],
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': 'db.sqlite3',
                }
            }
        )
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Le settings module de ton projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'script_perso.settings')

from django.core.management import execute_from_command_line

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
    configure_django()