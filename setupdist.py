# author: Taehong Kim
# email: peppy0510@hotmail.com


'''
PYPI Deployment Tools
'''


import os
import shutil
import subprocess
import sys


def command(cmd):
    proc = subprocess.Popen(cmd, shell=True)
    proc.communicate()


def increase_version_patch():
    with open('setup.py', 'r') as file:
        lines = file.read().split('\n')
        for i, line in enumerate(lines):
            if not line.strip(' ').startswith("version='"):
                continue
            key, value = line.strip(',').split('=')
            major, minor, patch = value.strip("'").split('.')
            lines[i] = "{key}='{major}.{minor}.{patch}',".format(
                **{'key': key, 'major': major, 'minor': minor, 'patch': str(int(patch) + 1)})

    with open('setup.py', 'w') as file:
        file.write('\n'.join(lines))


def setupdist(test=True, auto_increase_version_patch=True):
    if os.path.isdir('dist'):
        shutil.rmtree('dist')
    if auto_increase_version_patch:
        increase_version_patch()
    command('python setup.py sdist')
    command('twine upload -r {target} dist/*'.format(
        **{'target': 'test' if test else 'pypi'}))


if __name__ == '__main__':
    setupdist(test='test' in sys.argv)
