# pylint: disable=c0111
from _gitversion import get_version
try:
    from setuptools import setup
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup
import sys


def install_requires():
    _install_requires = ''
    if sys.version_info <= (3, 0):
        _install_requires = ['ipaddr']
    return _install_requires


setup(
    name='network-docopt',
    version=get_version(),
    description="Network Docopt",
    url="https://github.com/CumulusNetworks/NetworkDocopt",
    author='Cumulus Networks',
    author_email='ce-ceng@cumulusnetworks.com',
    license="MIT",
    py_modules=['network_docopt'],
    install_requires=install_requires(),
    scripts=['bin/network-docopt-example'],
    data_files=[('usr/share/bash-completion/completions',
                 ['completions/network-docopt-example'])],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ]
)
