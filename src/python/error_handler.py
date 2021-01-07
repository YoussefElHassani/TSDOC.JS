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
    # Packages dictionary
    packages_dict = {}

    for file_name, error in log.items():
        dir_name = os.path.dirname(file_name)

        if error['error_name'] == 'MODULE_NOT_FOUND':
            message = error['message']
            module_name = re.search(r'''(?<=')\s*[^']+?\s*(?=')''', message).group()
            # First try to download its associated npm package
            
            if module_name[0] == ".":
                # For now ignore
                # TODO: add aggregations of files per dir / maybe a code injection?
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
                packages_dict[dir_name]= module_name
                continue
            
            else:
                packages_dict[dir_name]= module_name
    return packages_dict

def install_npm_packages(packages_dict):

    for prefix, package in packages_dict.items():
        # Creating an empty npm-modules sub directory

        npm_install_cmd = "npm install --prefix " + prefix + " " + package
        ShCommand(npm_install_cmd, logger, "npm-installer", 3600).run()

def reference_errors_handler(log: dict):
    """[summary]

    Args:
        log (dict): [description]
    """
    pattern = "*.js"
    for file_name, error in log.items():
        dir_name = os.path.dirname(file_name)
        all_scripts_path = []
        if error['error_name'] == 'ReferenceError':
            for path, subdirs, files in os.walk(dir_name):
                for name in files:
                    if fnmatch(name, pattern):
                        all_scripts_path.append(os.path.join(path, name))

            # Removing files that contain "jalangi"
            filtered_paths = [i for i in all_scripts_path if 'node_modules' not in i]
            filtered_paths = [i for i in filtered_paths if 'jalangi' not in i]
  
            # Open file3 in write mode 
            with open(file_name, 'w') as outfile:
            
                # Iterate through list 
                for files in filtered_paths: 
            
                    # Open each file in read mode 
                    with open(files) as infile: 
            
                        # read the data from file1 and 
                        # file2 and write it in file3 
                        outfile.write(infile.read()) 
            
                    # Add '\n' to enter data of file2 
                    # from next line 
                    outfile.write("\n")
            infile.close()
            outfile.close()
    
    return packages_dict
    


# extract single names
# extract js files
# extract other type of files
packages_dict = modules_error_handler(log)
#install_npm_packages(packages_dict)
reference_errors_handler(log)