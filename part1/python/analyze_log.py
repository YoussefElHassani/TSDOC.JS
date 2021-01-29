import os
import re
import json
import ast

from itertools import chain
from collections import Counter
from error_graph import construct_graph, draw_graph, preprocess_graph

path = './log/info.log'

log_data= []
with open(path) as log_file:
    for line in log_file:
        log_data.append(json.loads(line[:-2]))

# Initializing error / success count
error_count = 0
success_count = 0

# initializing error type dictionary
error_dict = {}
# Initialiring error messages dictionary
error_messages = {}

# Successful dir runtime info
success_files = []

log = {}
# pass data to log dictionary
for record in log_data:
    file_path = record["data"][0]["file"]
    file_path = file_path.replace("_babel","")  
    exception = record["data"][0]["wrappedExceptionVal"]
    flag = record["data"][0]["flag"]
    if 'node_modules' in file_path:
        continue
    if file_path not in log:
        log[file_path] = {}
        log[file_path]['exception'] = exception
        log[file_path]['flag'] = flag

for file_name, file_dict in log.items():    
    flag = file_dict["flag"]
    exception = file_dict["exception"]
    

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
        success_files.append(file_name.rsplit('/', 1)[0])

# Write error dict to a file
with open('./log/log_analysis_babel.json', 'w') as fp:
    json.dump(error_dict, fp, indent=4)
    
print("Total number of errors: " + str(error_count))
print("Total number of successes: " + str(success_count))
"""
# Draw graphs per error message
for error_name, messages in error_messages.items():
    graph = construct_graph(messages)
    graph = preprocess_graph(graph, threshold = 0)
    title = error_name
    draw_graph(graph, title)
"""

success_files = list(dict.fromkeys(success_files))

for file_ in success_files:
    print(file_)
    
print(len(success_files))