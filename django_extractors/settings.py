import os

from django_path import DJANGO_PATH

settings_path = os.path.join(DJANGO_PATH, 'conf', 'global_settings.py')
variables = ''

with open(settings_path, 'r') as settings_file:
    for line in settings_file:
        if not line.startswith('#'):
            if '=' in line:
                split_line = line.split(' = ')
                variables += split_line[0] + '|'

variables = variables.lstrip('gettext_noop|').rstrip('|')
print(variables)
