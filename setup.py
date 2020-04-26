from setuptools import setup

from python_dwd import __version__

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='python_dwd',
    version=__version__,
    description='A module for accessing data of the german weather service',
    license='MIT',
    long_description=long_description,
    author='Benjamin Gutzmann|gutzemann@gmail.com, '
           'Daniel Lassahn|daniel.lassahn@meteointelligence.de',
    packages=['python_dwd'],
    install_requires=['pandas',
                      'tables',
                      'pathlib',
                      'zipfile',
                      'scipy',
                      'numpy',
                      'h5py',
                      'requests',
                      'lxml']
)
