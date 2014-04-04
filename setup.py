#!/usr/bin/env python

from distutils.core import setup, Command
from unittest import TextTestRunner, TestLoader
import os
import os.path


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        retval = os.system('python -m test')
        if retval != 0:
            raise Exception('tests failed')


setup(
    name='tornado-proxy',
    version='0.1',
    description='Simple asynchronous HTTP proxy',
    url='http://senko.net/en/',
    author='Senko Rasic',
    author_email='senko.rasic@dobarkod.hr',
    cmdclass={
        'test': TestCommand
    },
    install_requires=['tornado'],
    packages=['tornado_proxy'],
)
