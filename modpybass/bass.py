__version__ = '0.1'
__author__ = 'Taehong Kim'
__email__ = 'peppy0510@hotmail.com'
__license__ = 'BSD'
__doc__ = '''
bass_module, func_type = bass.load(__file__)
'''

import ctypes
import os
import platform
import sys


def load(name='bass'):
    name = os.path.splitext(os.path.basename(name))[0]
    if name.startswith('py'):
        name = name[2:]
    lib = os.path.join(os.path.dirname(__file__), 'lib')
    architecture = 'x64' if platform.machine().endswith('64') else 'x86'

    system_platform = sys.platform.lower()

    if system_platform.startswith('win'):
        extension = ['', '.dll']
    elif system_platform == 'darwin':  # macOS
        extension = ['lib', '.dylib']
    else:  # Linux and other Unix-like
        extension = ['lib', '.so']

    filename = name.join(extension)
    path = os.path.join(lib, architecture, filename)

    if os.path.isfile(path):
        try:
            if system_platform.startswith('win'):
                bass_module = ctypes.WinDLL(path)
                func_type = ctypes.WINFUNCTYPE
            else:
                bass_module = ctypes.CDLL(path, mode=ctypes.RTLD_GLOBAL)
                func_type = ctypes.CFUNCTYPE
            return bass_module, func_type
        except Exception as e:
            # It's good practice to log the error or handle it more gracefully
            print(f"Error loading BASS module {filename}: {e}")
            pass
    raise FileNotFoundError('Failed to load BASS module "%s" at %s' % (filename, path))


if __name__ == '__main__':
    bass_module, func_type = load('bass')