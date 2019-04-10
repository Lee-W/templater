#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup, Extension


setup(
    name='templater3',
    version='0.5.0',
    description=(
        'Extract template (a pattern) from strings and parse other'
        'strings with this pattern.'
    ),
    long_description=open('README.rst').read(),
    author=u'Álvaro Justen, Wei Lee',
    author_email='alvarojusten@gmail.com, cl87654321@gmail.com',
    url='https://github.com/Lee-W/templater',
    py_modules=['templater3'],
    ext_modules=[
        Extension('_templater', ['templater.c'])
    ],
    keywords=[
        'template', 'reversed template', 'template making', 'wrapper induction'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
