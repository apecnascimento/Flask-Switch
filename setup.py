"""
Flask-RouteBuilder
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-RouteBuilder',
    version='1.0',
    url='',
    license='MIT',
    author='apecnascimento',
    author_email='apecnascimento@gmail.com',
    description='Blueprint route builder for flask',
    long_description=__doc__,
    py_modules=['flask_route_builder'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)