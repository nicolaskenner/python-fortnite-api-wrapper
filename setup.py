from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fortnite',
    version='0.0.8',
    description='The Python Fortnite API Wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nicolaskenner/python-fortnite-api-wrapper',
    author='Nicolas Kenner',
    author_email='nick@nicolaskenner.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests >= 2.20.0']
)