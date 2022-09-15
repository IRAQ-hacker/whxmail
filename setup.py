import setuptools
from whxmail import __version__

with open('README.md', 'r') as fh:
    long_description = fh.read()
with open('requirements.txt','r') as fr:
    requires = fr.read().split('\n')

setuptools.setup(
    name='whxmail',
    version=__version__,
    author='rashid karim',
    author_email='rhpsilver@gmail.com',
    description='this library for checkers programming , with emails - gmail , yahoo , hotmail , autlook, by dev rashid karim',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iraq-hacker/whxmail',
    packages=['whxmail'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License'],
    install_requires=requires,
)