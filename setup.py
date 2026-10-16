from setuptools import find_packages,setup  
from typing import List 

# create a function becz we dont want to install all the dependencies manually 
def get_requiremets()-> List[str]: 
    requirements_list : List[str] = [] 

    return requirements_list




setup(
    name="sensor",
    version="0.0.1",
    author="sitesh",
    author_email="siteshjaisujaiswal@gmail.com",
    packages=find_packages(), 
    install_requires =get_requiremets(),
)