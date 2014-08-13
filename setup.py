from os import path
import codecs
from setuptools import setup


def read(*parts):
    filename = path.join(path.dirname('__file__'), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


setup(
    name='pytest-autoscenarios',
    version='0.1',
    description='Param your tests through docstrings',
    author='Dan Claudiu Pop',
    author_email='danclaudiupop@gmail.com',
    maintainer='Dan Claudiu Pop',
    maintainer_email='danclaudiupop@gmail.com',
    url='http://github.com/danclaudiupop/pytest-autoscenarios',
    py_modules=['pytest_autoscenarios'],
    long_description=read('README.md'),
    install_requires=['pytest>=2.6.1'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    entry_points={'pytest11': ['autoscenarios = pytest_autoscenarios']}
)
