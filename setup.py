import os
import re
import shutil
import sys

try:
    from setuptools import setup, Command
    from setuptools.extension import Extension
    #from Cython.Build import cythonize
except ImportError:
    raise RuntimeError('setuptools is required')

def read_file(*paths):
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, *paths)) as f:
        return f.read()

PACKAGE = 'pvlib'
PACKAGES = ['pvlib', 'pvlib.spa_c_files']

# check python version.
if sys.version_info[:2] != (2, 7):
    sys.exit('%s requires Python 2.7.x' % PACKAGE)

SHORT_DESC = 'Python port of the PVLIB package'

AUTHOR = 'Dan Riley, Clifford Hanson, Rob Andrews, github contributors' # look at pandas/ipython/etc to see how they automatically generate this
AUTHOR_EMAIL = 'Rob.Andrews@calamaconsulting.ca'

LICENSE = 'The BSD 3-Clause License'

URL = 'https://github.com/Sandia-Labs/PVLIB_Python'
# DOWNLOAD_URL = 'https://github.com/Sandia-Labs/PVLIB_Python/tarball/0.1'

# get version information.
versionfile = PACKAGE + "/_version.py"
verstrline = open(versionfile, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    VERSION = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (versionfile,))

long_description = open('README.txt').read()
# proposal for the future:
# Get long_description from index.rst:
# long_description = read_file('docs', 'index.rst')
# long_description = long_description.strip().split('split here', 1)[0]
# long_description += "\n\n" + read_file('docs', 'changes.rst') # Add release history

setuptools_kwargs = {
    'zip_safe': False,
    'install_requires': ['numpy >= 1.7',
                         'scipy >= 0.14.0',
                         'pandas >= 0.13',
                         'pyephem',
                         'matplotlib',
                         'ipython >= 2.0',
                         'pyzmq >= 2.1.11',
                         'jinja2',
                         'tornado'
                         ],
    'scripts':[],
    'include_package_data': True
}

setup(
    name=PACKAGE,
    version=VERSION,
    description=SHORT_DESC,
    long_description=long_description,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=URL,
    packages=PACKAGES,
    ext_modules=[Extension("pvlib/spa_c_files/spa_py", ["pvlib/spa_c_files/spa_py.pyx",'pvlib/spa_c_files/spa.c'])],
    #ext_modules=[Extension("pvlib.spa_c_files.spa_py", ["pvlib/spa_c_files/spa_py.pyx",'pvlib/spa_c_files/spa.c'])],
    #ext_modules=cythonize([Extension("spa_py", ["spa_py.pyx",'spa.c'])])
    **setuptools_kwargs)
    
# pip install -e . --upgrade --force-reinstall --no-deps

# setup(
#     name='pvlpy',
#     version='0.1',
#     author='Dan Riley, Clifford Hanson and Rob Andrews',
#     author_email='Rob.Andrews@calamaconsulting.ca',
#     packages=['pvlpy','pvlpy.test'],
#     license='The BSD 3-Clause License',
#     url = 'https://github.com/Sandia-Labs/PVLIB_Python',
#     download_url = 'https://github.com/Sandia-Labs/PVLIB_Python/tarball/0.1',
#     long_description=open('README.txt').read(),
# )