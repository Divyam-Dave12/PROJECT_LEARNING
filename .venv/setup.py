from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements =[req.replace("\n","") for req in requirements]
    # Remove any whitespace characters like `\n` at the end of each line
    return [req.strip() for req in requirements if req.strip()]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name = 'ml_project',
    version = '0.1.0',
    author = 'Divyam Dave',
    author_email= 'divyamdave2003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirments.txt'),
    description='This is my first machine learning project'
)    
