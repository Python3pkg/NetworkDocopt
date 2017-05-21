# pylint: disable=c0111
from .version import __VERSION__
try:
    from setuptools import setup
except ImportError:
    from . import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup
import sys
import os
import io


def read_contents(fname='README.rst'):
    return io.open(os.path.join(os.path.dirname(__file__),
                                fname), encoding="utf-8").read()


def install_requires():
    _install_requires = ''
    if sys.version_info <= (3, 0):
        _install_requires = ['ipaddr']
    return _install_requires


setup(
    name='network-docopt',
    version=__VERSION__,
    description="Network Docopt",
    url="https://github.com/CumulusNetworks/NetworkDocopt",
    long_description=read_contents(),
    author='Cumulus Networks',
    author_email='ce-ceng@cumulusnetworks.com',
    license="MIT",
    py_modules=['network_docopt'],
    install_requires=install_requires(),
    scripts=['bin/network-docopt-example'],
    data_files=[('share/bash-completion/completions',
                 ['completions/network-docopt-example'])],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ]
)
