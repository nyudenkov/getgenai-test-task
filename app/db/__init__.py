from app.settings import settings


MODELS = ['app.db.models', 'aerich.models']

TORTOISE_ORM = {
    'connections': {'default': str(settings.db_url)},
    'apps': {
        'models': {
            'models': MODELS,
            'default_connection': 'default',
        },
    },
}
