from setuptools import find_packages,setup
from typing import List

should_not_come = '-e .'

def get_requirments(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","")for req in requirments]

        if should_not_come in requirments:
            requirments.remove(should_not_come)

    return requirments


setup(
name='mlprojects',
version='0.0.1',
author='Haris',
author_email='harisrp82@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirments.txt')
)