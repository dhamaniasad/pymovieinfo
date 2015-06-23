from setuptools import setup
import pymovieinfo
import os

setup(
    name='pymovieinfo',
    version=pymovieinfo.__version__,
    description='Get information about any movie from the command line',
    author='Asad Dhamani',
    author_email='dhamaniasad+code@gmail.com',
    url='https://github.com/dhamaniasad/pymovieinfo',
    license='Unlicense',
    py_modules=['pymovieinfo'],
    entry_points={
        'console_scripts': [
            'movieinfo = pymovieinfo:command_line_runner'
        ]
    }
)
