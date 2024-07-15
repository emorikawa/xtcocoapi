from setuptools import setup, Extension
import numpy as np

version_file = 'xtcocotools/version.py'

def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    import sys
    # return short version for sdist
    if 'sdist' in sys.argv or 'bdist_wheel' in sys.argv:
        return locals()['short_version']
    else:
        return locals()['__version__']

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"
# Note that the original compile flags below are GCC flags unsupported by the Visual C++ 2015 build tools.
# They can safely be removed.
ext_modules = [
    Extension(
        'xtcocotools._mask',
        sources=['./common/maskApi.c', 'xtcocotools/_mask.pyx'],
        include_dirs = [np.get_include(), './common'],
        extra_compile_args=[] # originally was ['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name='xtcocotools',
    packages=['xtcocotools'],
    package_dir = {'xtcocotools': 'xtcocotools'},
    install_requires=['matplotlib>=2.1.0',
        'numpy>=1.19.5; python_version == "3.6"',
        'numpy>=1.20.0; python_version >= "3.7"'],
    setup_requires=['setuptools>=18.0',
        'cython>=0.27.3',
        'numpy>=1.19.5; python_version == "3.6"',
        'numpy>=1.20.0; python_version >= "3.7"'],
    version=get_version(),
    description="Extended COCO API",
    url="https://github.com/jin-s13/xtcocoapi",
    ext_modules= ext_modules
)
