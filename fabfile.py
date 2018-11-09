import os
from fabric.api import local


ENVIRONMENT_NAME = 'venv'

REQUIRENMENTS_FILE_PATH = 'requirenments.pip'


def _get_kwargs_string(kwargs):
    return ' '.join(
        map(
            lambda key: f'--{key} {kwargs.get(key)}',
            kwargs
        )
    )


def _get_args_string(args):
    return ' '.join(
        map(
            lambda itm: f'--{itm}',
            args
        )
    )


def runserver(addrport='', *args, **kwargs):
    local(
        f'''
        cd djangoProject\ServerAutomarket
        python manage.py runserver {addrport} {_get_args_string(args)} {_get_kwargs_string(kwargs)}
        '''
    )


def startapp(name, *args, **kwargs):
    local(
        f'''
        cd ServerAutomarket
        python manage.py startapp {name} {_get_args_string(args)} {_get_kwargs_string(kwargs)}
        '''
    )


def makemigrations(*args, **kwargs):
    local(
        f'''
        cd ServerAutomarket
        python manage.py makemigrations {_get_args_string(args)} {_get_kwargs_string(kwargs)}
        '''
    )


def migrate(*args, **kwargs):
    local(
        f'''
        cd ServerAutomarket
        python manage.py migrate {_get_args_string(args)} {_get_kwargs_string(kwargs)}
        '''
    )


def createsuperuser(**kwargs):
    local(
        f'''
        cd ServerAutomarket
        python manage.py createsuperuser {_get_kwargs_string(kwargs)}
        '''
    )


def shell(*args, **kwargs):
    local(
        f'''
        cd ServerAutomarket
        python manage.py shell {_get_args_string(args)} {_get_kwargs_string(kwargs)}
        '''
    )


def install(module_name=None, *args, **kwargs):
    if not module_name:
        local(f'pip install -r {REQUIRENMENTS_FILE_PATH}')
    else:
        local(f'pip install {module_name} {_get_args_string(args)} {_get_kwargs_string(kwargs)}')
        local(f'pip freeze > {REQUIRENMENTS_FILE_PATH}')


def init():
    if not os.path.exists(REQUIRENMENTS_FILE_PATH):
        local(f'virtualenv {ENVIRONMENT_NAME}')
        local(
            f'''
            . {ENVIRONMENT_NAME}djangoProject/getstarted/Scripts/activate
            pip freeze > {REQUIRENMENTS_FILE_PATH}
            '''
        )