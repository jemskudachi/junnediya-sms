from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Add this line:
ROOT_URLCONF = 'sms_project.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
