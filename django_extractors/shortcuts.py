import os
import re

from django_path import DJANGO_PATH

shortcuts_path = os.path.join(DJANGO_PATH, 'shortcuts.py')
shortcuts = ''

with open(shortcuts_path, 'r') as shortcuts_file:
    for line in shortcuts_file:
        if not line.startswith('#'):
            if line.startswith('def'):
                function_name = re.search('(def)\s((?!_).*)\(', line)
                if function_name:
                    shortcuts += function_name.group(2) + '|'

shortcuts = shortcuts.rstrip('|')
print(shortcuts)
