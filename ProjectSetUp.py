# Importing dependencies
import os
import sys
import subprocess


# Update pip package
subprocess.check_call([sys.executable, '-m', 'pip3', 'install', '--upgrade', 'pip'])
# Install all required packages
#subprocess.check_call([sys.executable, '-m', 'pip3', 'install', '-r', "requirements.txt"])

# Set Up Folder Structure
def SetUp(name):
    # Create folder "data" to store test and back up files
    isExist = os.path.exists("data")
    if isExist == True:
        print("data directory already exists!")
    if not isExist:
        os.mkdir("data")
        print("The data directory is created!")

    # Create folder notebooks to store jupyter notebook files
    isExist = os.path.exists("notebooks")
    if isExist == True:
        print("notebook directory already exists!")
    if not isExist:
        os.mkdir("notebooks")
        print("The notebooks directory is created!")

    # Create folder to store libraries
    isExist = os.path.exists("lib")
    if isExist == True:
        print("lib directory already exists!")
    if not isExist:
        os.mkdir("lib")
        print("The lib directory is created!")

    # Create folder "parameters" to store config.json file which will have all necessary elements to access to database
    isExist = os.path.exists("parameters")
    if isExist == True:
        print("parameters directory already exists!")
    if not isExist:
        os.mkdir("parameters")
        print("The parameters directory is created!")

    # Create notebook "SandBox.ipynb" for any further testing and development
    isExist = os.path.exists("notebooks\SandBox.ipynb")
    if isExist == True:
        print("SandBox.ipynb notebook already exists!")
    if not isExist:
        with open("notebooks\SandBox.ipynb", mode='a'): pass
        print("The SandBox.ipynb notebook is created!")

    # Create "ReadMe.MD" file to define the project
    isExist = os.path.exists("ReadMe.md")
    if isExist == True:
        print("ReadMe file already exists!")
    if not isExist:
        with open("README.md", mode='a'): pass
        print("The README.md file is created!")

if __name__ == '__main__':
    SetUp('PyCharm')