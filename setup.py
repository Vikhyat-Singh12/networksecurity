from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """
        this function will return the requirements of the project
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines of the file
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore empty line and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("Hey requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Vikhyat Singh",
    author_email="singhvikhyatmzp.9@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)