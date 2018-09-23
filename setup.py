#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)


extras_require = {
    'lint': [
        'flake8>=3.5.0,<4.0.0',
    ],
    'test': [
        'pytest>=3.2.1,<4.0.0',
        'pytest-xdist>=1.22.2,<2',
        'eth-hash[pycryptodome]>=0.1.4,<1.0.0',
    ],
    'dev': [
        'bumpversion>=0.5.3,<1.0.0',
        'tox>=2.9.1,<3.0.0',
        'wheel>=0.30.0,<1.0.0',
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +
    extras_require['test'] +
    extras_require['lint']
)


setup(
    name='moac-tester',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='0.1.0',
    description="""Tools for testing Moac applications.""",
    long_description_markdown_filename='README.md',
    author='Zhenglong Cai',
    author_email='caizl2002@hotmail.com',
    url='https://github.com/wanpixiaozi/moac-tester',
    include_package_data=True,
    install_requires=[
        "toolz>0.8.2,<1;implementation_name=='pypy'",
        "cytoolz>=0.8.2,<1.0.0;implementation_name=='cpython'",
        "eth-utils>=1.0.1,<2.0.0",
        "rlp>=0.6.0,<2.0.0",
        "semantic_version>=2.6.0,<3.0.0",
        "eth-keys>=0.2.0-beta.3,<0.3.0",
        "eth-abi>=1.0.0-beta.1,<2",
    ],
    extras_require=extras_require,
    setup_requires=['setuptools-markdown'],
    # py_modules=['moac_tester'],
    license="MIT",
    zip_safe=False,
    keywords='moac',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
