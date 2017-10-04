from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    currentLicense = f.read()

setup(
    name='NeuronalNetworkTest',
    version='0.0.1',
    description='Random project to play with neuronal networks',
    long_description=readme,
    author='Fantin BIBAS',
    author_email='fantin.bibas@epitech.eu',
    url='https://github.com/FantinBibas',
    license=currentLicense,
    packages=find_packages(exclude=('tests', 'docs'))
)