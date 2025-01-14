from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements
    
    """
    requirement_list=[]
    try:
        with open("requirements.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                requirement=line.strip()
                
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found.")

    return requirement_list


setup(
    name="network secutiry",
    version="0.0.1",
    author="Kapish",
    author_email="kapishashtankar10@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)