from setuptools import find_packages, setup
from typing import List


def get_requirements()->List[str]:
    """
    This function will return list of requirements

    """
    requirements_list: List[str] = []
    return requirements_list


setup(
    name ="text-generation",
    version = "0.0.1",
    author = "iNeuron",
    author_email ="shubhamsharma@ineuron.ai",
    packages = find_packages(),
    install_requires = get_requirements()

)
