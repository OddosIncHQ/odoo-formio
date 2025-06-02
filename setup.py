from setuptools import setup, find_packages

setup(
    name='formiodata',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Oddos Inc',
    description='Formio data wrapper for Odoo integration',
    url='https://github.com/OddosIncHQ/odoo-formio',
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)
