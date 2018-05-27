import re

from setuptools import setup, find_packages

with open('vendor_files/__init__.py') as f:
    metadata = dict(re.findall(r'__(.*)__ = [\']([^\']*)[\']', f.read()))

setup(
    name=metadata['title'],
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    maintainer=metadata['author'],
    maintainer_email=metadata['email'],
    license=metadata['license'],
    url='https://github.com/aipescience/django-vendor-files',
    description=u'A small extension to download css and js vendor files from CDNs and host them locally.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'Django>=1.11',
        'requests'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages()
)
