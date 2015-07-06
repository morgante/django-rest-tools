from setuptools import setup

from django_rest_tools import get_version


def get_install_requires():
    requirements = []
    for line in open('requirements.txt').readlines():
        if line.startswith('#') or line == '' or line.startswith('http') or line.startswith('git'):
            continue
        requirements.append(line)
    return requirements

setup(
    name='django-rest-tools',
    summary=open('README.rst').read(),
    version=get_version(),
    license='GPLv3',
    author='Quique Porta',
    author_email='quiqueporta@gmail.com',
    description='Tools for Django Rest Framework',
    url='https://github.com/quiqueporta/django-rest-tools',
    download_url='https://github.com/quiqueporta/django-rest-tools/releases',
    keywords=['django', 'djangorestframework', 'tools'],
    packages=['django_rest_tools'],
    install_requires=get_install_requires(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
