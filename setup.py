from setuptools import setup, find_packages
from os import path

SCRIPT_DIR = path.abspath(path.dirname(__file__))

with open(path.join(SCRIPT_DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='prp1',
    python_requires='>=3',
    version='1.0.0',
    description='This package is a part of our research process regarding issue #1884',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/dustico/prp1',
    author='Dustico Research',
    author_email='research@dusti.co',
    license='Apache v2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='prp1 dustico research',
    packages=['prp1'],
    install_requires=[]
)
