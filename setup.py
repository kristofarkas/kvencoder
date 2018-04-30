from setuptools import setup, find_packages

setup(
    name='kvencoder',

    version='0.0.1.dev1',

    description='Key value encoding',

    long_description='Copy from README file',

    url='http://ccs.chem.ucl.ac.uk',

    author='Kristof Farkas-Pall',

    requires=['pyyaml'],

    packages=find_packages(),

    include_package_data=True,
)
