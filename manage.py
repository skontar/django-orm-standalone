import django
from django.conf import settings
from django.core.management import execute_from_command_line


def init_django():
    if settings.configured:
        return

    settings.configure(
        DEBUG=True,
        INSTALLED_APPS=[
            'db',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        },
        DEFAULT_AUTO_FIELD='django.db.models.AutoField'
    )
    django.setup()


if __name__ == "__main__":
    init_django()
    execute_from_command_line()
