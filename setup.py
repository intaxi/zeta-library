#!/usr/bin/env python
import os

from setuptools import setup, find_packages

from zetalinker import VERSION, PROJECT


def read( fname ):
    try:
        return open( os.path.join( os.path.dirname( __file__ ), fname ) ).read()
    except IOError:
        return ''

MODULE_NAME = 'zetalinker'
PACKAGE_DATA = []

for root, dirs, files in os.walk( os.path.join( MODULE_NAME, 'zetalib' ) ):
    for filename in files:
        PACKAGE_DATA.append("%s/%s" % ( root[len(MODULE_NAME)+1:], filename ))

META_DATA = dict(
    name=PROJECT,
    version=VERSION,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='GNU LGPL',

    author='Kirill Klenov',
    author_email='horneds@gmail.com',

    url=' http://github.com/klen/zeta-library',

    platforms=('Any'),

    packages=find_packages(),
    package_data = { '': PACKAGE_DATA, },

    entry_points={
        'console_scripts': [
            'zeta = zetalinker.parse:main',
        ]
    },
)

if __name__ == "__main__":
    setup( **META_DATA )
