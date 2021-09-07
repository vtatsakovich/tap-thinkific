#!/usr/bin/env python

from setuptools import setup

setup(name='tap-thinkific',
      version='1.0.0',
      description='`tap-thinkific` is a Singer tap for Thinkific, built with the Meltano SDK for Singer Taps.',
      author='Roman Chessnocow',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      install_requires=[
        'attrs==16.3.0',
        'singer-python==5.10.0',
        'requests==2.23.0',
        'backoff==1.8.0',
        'requests_mock==1.3.0',
      ],
      extras_require={
          'dev': [
              'pylint',
              'ipdb',
              'nose',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-thinkific=tap_thinkfic:main
    ''',
    packages=['tap_thinkific'],
    package_data = {
        'schemas': [
            'tap_thinkific/schemas/*.json',
        ],
    },
    include_package_data=True
)
