#!/usr/bin/env python
"""
sentry-useremail
================
:copyright: (c) 2015 Dave McLain
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages

install_requires = [
    'sentry>=7.1.4',
]

setup(
    name='sentry-useremail',
    version='0.1.0',
    author='Dave McLain',
    author_email='github@davemclain.com',
    url='http://github.com/dmclain/sentry-useremail',
    description='A Sentry extension which allows rule actions to send to individual users',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'sentry_useremail = sentry_useremail',
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
