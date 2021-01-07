from fnmatch import fnmatch
from shell_command import ShCommand 

import logging
import sys
import os
import json
import re

# Configuring logger
logging.basicConfig()
logger = logging.getLogger()
# Categorize errors by type

# get file names from first file
path = './log/info_babel.log'
error_lines= []
with open(path) as log_file:
    for line in log_file:
        error_lines.append(json.loads(line[:-2]))
        

# Initialize log variable
log = {}

# Printing error name
for record in error_lines:
    file_path = record["data"][0]["file"]
    # remove the babel part from the file names
    file_path = file_path.replace("_babel","")
    # Get the exception from the recorded lines
    exception = record["data"][0]["wrappedExceptionVal"]
    flag = record["data"][0]["flag"]

    # Ignore node_modules file
    if 'node_modules' in file_path:
        continue

    # Adding the relevant fields to the log dictionary
    if(flag == "Error"):
        # Once the exception is not none since the file returns an error, we convert it to a  JSON file
        exception = dict(json.loads(exception))
        log[file_path] = {}
        
        try:
            error_name = exception["exception"]["code"]
        except:
            error_name = exception["exception"]["name"]
            
        log[file_path]['error_name'] = error_name
        log[file_path]['message'] = exception["exception"]['message']
        log[file_path]['flag'] = flag

       
def modules_error_handler(log: dict):
    """[summary]

    Args:
        log (dict): [description]
    """
    path = '../dts-generate-results/results/4_extract-code/code'
    # Defining modules not found errors
    modules_errors ={}
    # Packages dictionary
    packages_dict = {}
    cnt = 0
    for file_name, error in log.items():
        dir_name = os.path.dirname(file_name)

        if error['error_name'] == 'MODULE_NOT_FOUND':
            # modules_errors[file_name]
            message = error['message']
            module_name = re.search(r'''(?<=')\s*[^']+?\s*(?=')''', message).group()
            # First try to download its associated npm package
            
            if module_name[0] == ".":
                # Import all js files in the same directory
                # Reexcute code
                #print(item)
                continue

            elif fnmatch(module_name, "*/*/*"):
                # Keep the first module name
                target_index = module_name.index('/')
                module_name = module_name[:target_index]
                packages_dict[dir_name]= module_name
                continue
            
            elif fnmatch(module_name, "*.js"):
                # Import all js files in the same directory
                # Reexcute code
                print(module_name)
                continue
            
            else:
                packages_dict[dir_name]= module_name
        
def install_npm_packages(packages_dict):

    for prefix, package in packages_dict.items():
        # Creating an empty npm-modules sub directory

        npm_install_cmd = "npm install --prefix " + prefix + " " + package
        ShCommand(npm_install_cmd, logger, "npm-installer", 3600).run()

def reference_errors_handler(log: dict):
    print("hi")


# extract single names
# extract js files
# extract other type of files
modules_error_handler(log)
