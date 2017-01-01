#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='chatterbot_dice',
    version=0.1,
    description='Chatterbot dice add on',
    author='PKnull',
    author_email='louis.grenzebach@gmail.com',
    url='https://github.com/pknull/chatterbot-dice',
    packages=[
        'chatterbot_dice',
    ],
    package_dir={'chatterbot-dice': 'chatterbot_dice'},
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    keywords='chatterbot dice'
)