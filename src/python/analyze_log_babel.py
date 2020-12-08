import os
import re
import json
import ast

from itertools import chain
from collections import Counter
from error_graph import construct_graph, draw_graph

path = './log/info.log'

# 1. Extracting the common files
# get file names from first file
path = './log/info.log'
data_1 = []
with open(path) as log_file:
    for line in log_file:
        data_1.append(json.loads(line[:-2]))
        
files_1 = []       
for record in data_1:
    file_path = record["data"][0]["file"]
    if 'node_modules' in file_path:
        continue
    files_1.append(file_path)

# get file names from second file

path = './log/info_babel.log'

data_2 = []
with open(path) as log_file:
    for line in log_file:
        data_2.append(json.loads(line[:-2]))
files_2 = []

for record in data_2:
    file_path = record["data"][0]["file"]
    #if 'node_modules' in file_path:
    #    continue
    file_path = file_path.replace("_babel","")        
    files_2.append(file_path)



list1_as_set = set(files_1)
intersection = list1_as_set.intersection(files_2)


# Initializing error / success count
error_count = 0
success_count = 0

# initializing error type dictionary
error_dict = {}
# Initialiring error messages dictionary
error_messages = {}

log = {}
# pass data to log dictionary
for record in data_2:
    file_path = record["data"][0]["file"]
    file_path = file_path.replace("_babel","")  
    exception = record["data"][0]["wrappedExceptionVal"]
    flag = record["data"][0]["flag"]
    if 'node_modules' in file_path:
        continue
    if file_path not in intersection:
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

# Write error dict to a file
with open('./log/log_analysis_babel.json', 'w') as fp:
    json.dump(error_dict, fp, indent=4)
    
print("Total number of errors: " + str(error_count))
print("Total number of successes: " + str(success_count))

"""
# Draw graphs per error message
for error_name, messages in error_messages.items():
    graph = construct_graph(messages)
    title = error_name
    draw_graph(graph, title)
"""
"""
cnt = 0
for file_name, file_dict in log.items():
    if file_dict["flag"] == "Error":
        exception = file_dict["exception"]
        exception_dict = json.loads(exception)
        error_name = exception_dict["exception"]["name"]
        error_message = exception_dict["exception"]["message"]
        if error_name == "SyntaxError":
            print(file_name)
            print(error_message)
            print()
            cnt += 1
            if cnt > 5:
                break"""