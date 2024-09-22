from setuptools import find_packages, setup
from typing import List


Hypen_edot = '-e .'

def get_requirement(file_path:str)->List[str]:
    '''
    This Function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]
        if Hypen_edot in requirements:
            requirements.remove(Hypen_edot)
    return requirements


setup(
    name='Ml Project',
    version='0.0.1',
    author="Anish Dhakal",
    author_email="anish.dhakal54@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
    
    )