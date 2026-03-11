from setuptools import find_packages,setup

def get_requirements(filename):  # this function will read the requirements.txt file and return a list of requirements
    with open(filename, "r") as f:
        lines = f.readlines()
        requirements=[line.replace("\n","") for line in lines]

        if "-e ." in requirements:
            requirements.remove("-e .")
      
    return requirements
setup(
name='mlproject',
version='0.0.1',
author='Yekanth',
author_email="yekanthsai@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")

)