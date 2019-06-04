#!/usr/bin/env python

from setuptools import setup

setup(name='bitfinex-api-module',
      version='0.2.2',
      description='Bitfinex API client.',
      url='https://github.com/doghoc/bitfinex-api-py',
      install_requires=[
          'eventemitter==0.2.0',
          'asyncio==3.4.3',
          'websockets==7.0',
          'pylint==2.3.0',
          'pytest-asyncio==0.9.0',
          'six==1.12.0',
          'pyee==5.0.0',
          'aiohttp==3.4.4',
      ],
      packages=['bfxapi', 'bfxapi.models', 'bfxapi.websockets',
                'bfxapi.rest',  'bfxapi.utils', ]
      )