# coding: utf-8

from setuptools import setup, find_packages

NAME = 'bitmovin-api-sdk'
VERSION = '1.187.1'
DESCRIPTION = 'Python-Client which enables you to seamlessly integrate the Bitmovin API into your projects. Using this API client requires an active account.'
AUTHOR = 'Bitmovin Inc'
EMAIL = 'support@bitmovin.com'
URL = 'https://github.com/bitmovin/bitmovin-api-sdk-python'
LICENSE = 'MIT'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ['urllib3>=1.15,<1.26', 'six>=1.10', 'certifi', 'python-dateutil', 'pytz', 'requests>=2.22.0,<2.25.0']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    license=LICENSE,
    keywords=['Bitmovin', 'Bitmovin API Reference'],
    install_requires=REQUIRES,
    long_description=DESCRIPTION,
)
