import os


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='modpybass',
    version='0.0.2',
    author='Taehong Kim',
    author_email='peppy0510@hotmail.com',
    description=('modified pybass'),
    license='Apache License 2.0',
    keywords='bass',
    url='https://github.com/peppy0510/modpybass',
    packages=['modpybass'],
    package_data={
         'modpybass': ['lib/x86/*', 'lib/x64/*'],
    },
    long_description=read('README'),
    classifiers=[
        'Development Status :: Beta',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache License',
    ],
)
