from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requires = f.read().splitlines()

setup(
    name='create_aituber',
    version='0.1.0',
    author='t4ned4',
    author_email='taneda.bp@gmail.com',
    description='necessary libraries for create-aituber',
    url='https://github.com/t4ned4/create-aituber',
    packages=find_packages(),
    install_requires=requires,
)
