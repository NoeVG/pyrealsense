import ctypes
import sys
import os

os_name = sys.platform
lrs_suffix_mapping = {'darwin':'.dylib', 'linux':'.so', 'linux2':'.so'} # 'win':'.dll'}
rsu_suffix_mapping = {'darwin':'.so', 'linux':'.so', 'linux2':'.so'} # 'win':'.dll'}

try:
    lrs_suffix = lrs_suffix_mapping[os_name]
    rsu_suffix = rsu_suffix_mapping[os_name]
except KeyError:
    raise OSError('OS not supported.')

## hacky way to load "extension" module
def _find_extension_name():
    dirname = os.path.dirname(__file__)
    f_name = ''
    for f in os.listdir(dirname):
        if f.endswith(rsu_suffix):
            f_name = f
    return os.path.join(dirname, f_name)

## prevent crash for Sphinx when extension is not compiled before hand
try:
    rsutilwrapper = ctypes.CDLL(_find_extension_name())
except OSError:
    import warnings
    warnings.warn("rsutilwrapper not found.")
    rsutilwrapper = None

## import C lib
lrs = ctypes.CDLL('librealsense'+lrs_suffix)

