import os
import re
import json
import ast 

path = './log/info.log'

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

# Printing error name
for record in data:
    exception = record["data"][0]["wrappedExceptionVal"]
    flag = record["data"][0]["flag"]
    if flag == "Error":
        error_count += 1
        exception_dict = json.loads(exception)
        error_name = exception_dict["exception"]["name"]
        if(error_name == "Error"):
            try:
                error_name = exception_dict["exception"]["code"]
            except:
                error_name = exception_dict["exception"]["name"]

        if error_name not in error_dict:
            error_dict[error_name] = 1
        else:
            error_dict[error_name] += 1
    else: 
        success_count += 1

# Write error dict to a file
with open('./log/log_analysis.json', 'w') as fp:
    json.dump(error_dict, fp, indent=4)
    
print("Total number of errors: " + str(error_count))
print("Total number of successes: " + str(success_count))