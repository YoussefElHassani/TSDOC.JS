import os
import re
import json
import ast 

from itertools import chain
from collections import Counter

path = './log/info_babel.log'

# Reading files
data = []
with open(path) as log_file:
    for line in log_file:
        data.append(json.loads(line[:-2]))

# Initializing error / success count
error_count = 0
success_count = 0

# initializing error type dictionary
error_dict = {}
# Initialiring error messages dictionary
error_messages = {}

# Printing error name
for record in data:
    file_path = record["data"][0]["file"]
    if 'node_modules' in file_path:
        continue

    exception = record["data"][0]["wrappedExceptionVal"]
    flag = record["data"][0]["flag"]
    if flag == "Error":
        error_count += 1
        exception_dict = json.loads(exception)
        error_name = exception_dict["exception"]["name"]
        error_message = exception_dict["exception"]["message"]
        if(error_name == "Error"):
            try:
                error_name = exception_dict["exception"]["code"]
            except:
                error_name = exception_dict["exception"]["name"]
        # Adding error message to the error_messages dict
        if error_name not in error_messages:
            error_messages[error_name] = []
            error_messages[error_name].append(error_message)
        else:
            error_messages[error_name].append(error_message)

        # Counting the occurance of the error code
        if error_name not in error_dict:
            error_dict[error_name] = 1
        else:
            error_dict[error_name] += 1
    else: 
        success_count += 1

# Write error dict to a file
with open('./log/log_analysis_babel.json', 'w') as fp:
    json.dump(error_dict, fp, indent=4)
    
print("Total number of errors: " + str(error_count))
print("Total number of successes: " + str(success_count))
