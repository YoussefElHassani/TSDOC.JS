import json
import re

from fnmatch import fnmatch


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
    # Defining modules not found errors
    modules_errors ={}
    
    a = set()
    cnt = 0
    for file_name, error in log.items():
        #a.add(error['error_name'])
        if error['error_name'] == 'MODULE_NOT_FOUND':
            # modules_errors[file_name]
            message = error['message']
            module_name = re.search(r'''(?<=')\s*[^']+?\s*(?=')''', message).group()
            a.add(module_name)
 
    for item in a:
        print(item)
        if item[0] == ".":
            #print(item)
            continue
        
        elif fnmatch(item, "*.js"):
            continue
        
        elif fnmatch(item, "*/*/*"):
            #print(item)
            continue
        
# extract single names
# extract js files
# extract other type of files
modules_error_handler(log)