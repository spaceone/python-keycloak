# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='python-keycloak',
    version='0.1.0',
    url='https://github.com/marcospereirampj/python-keycloak',
    license='GNU General Public License - V3',
    author='Marcos Pereira',
    author_email='marcospereira.mpj@gmail.com',
    keywords='keycloak openid',
    description=u'python-keycloak is a Python package providing access to the Keycloak API.',
    packages=['keycloak'],
    install_requires=['requests==2.18.3', 'httmock==1.2.5'],
)