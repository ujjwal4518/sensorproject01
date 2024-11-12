from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    reqirements=[]
    with open(file_path) as file_obj:
        reqirements = file_obj.readlines()
        reqirements = [req.replace("\n","") for req in reqirements]
    
    
    if HYPEN_E_DOT in reqirements:
        reqirements.remove(HYPEN_E_DOT)
    return reqirements    



setup(
    name='Fault detection',
    version='0.0.1',
    author='ujjwal',
    author_email='ujjwaldwivedi567@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()

)