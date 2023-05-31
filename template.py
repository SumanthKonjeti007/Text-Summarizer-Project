# import os
# from pathlib import Path
# import logging

# #for logging information
# logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# project_name = "textSummarizer"

# """.github file for deployment, here we write CI CD yaml file
# helps you to cicd deployment, when we commit the code it will automatically takes your code from
# your github and it will do deployment in your cloud"""

# list_of_files = [
#     ".github/workflows/.gitkeep", #dummy reference file
#     f"src/{project_name}/__init__.py", #for import statements like from textSummarizer import x module. For this we need constructor file. When ever you are using local packages we need this constructor file.
#     f"src/{project_name}/components/__init__.py",
    
#     f"src/{project_name}/utils/__init__.py",
#     f"src/{project_name}/utils/common.py", #has all the utility functions.
    
#     f"src/{project_name}/logging/__init__.py",
    
#     f"src/{project_name}/config/__init__.py",
#     f"src/{project_name}/config/configuration.py"
    
#     f"src/{project_name}/pipeline/__init__.py", #have content about configuration prediction pipleline 
    
#     f"src/{project_name}/entity/__init__.py",
    
#     f"src/{project_name}/constants/__init__.py",
#     "config/config.yaml",
#     "params.yaml", #has all the model related parameters
#     "app.py",
#     "main.py",
#     "Dockerfile",
#     "requirements.txt",
#     "setup.py", #helps with local package setup
#     "research/trails.ipynb" 
# ]

# #Logic for creating the above folders
# for filepath in list_of_files:
#     #Convert the filepath to my specified Operating System format. To overcome / issues.
#     filepath = Path(filepath)
#     #split the folder and file
#     filedir, filename = os.path.split(filepath)

#     if filedir != "":
#         os.makedirs(filedir, exist_ok=True)
#         logging.info(f"Created directory: {filedir} for the file {filename}")
    
#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
#         with open(filepath,'w') as f:
#             pass
#             logging.info(f"Creating empty file: {filepath}")
#     else:
#         logging.info(f"{filepath} already exists")


import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")