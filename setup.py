from setuptools import find_packages,setup 




setup(
    name="sensor",
    version="0.0.1",
    author="sitesh",
    author_email="siteshjaisujaiswal@gmail.com",
    packages=find_packages(), 
    install_requires = ['pymongo']
)