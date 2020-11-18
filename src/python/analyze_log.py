import os
import re
import json
import ast 

from itertools import chain
from collections import Counter
from nltk.tokenize import wordpunct_tokenize

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
# Initialiring error messages dictionary
error_messages = {}

# Printing error name
for record in data:
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
with open('./log/log_analysis.json', 'w') as fp:
    json.dump(error_dict, fp, indent=4)
    
print("Total number of errors: " + str(error_count))
print("Total number of successes: " + str(success_count))

# Finding most common words per error code 
error_messages_tokens = {}
for key in error_messages:
    messages = error_messages[key]
    array = (Counter(chain.from_iterable(wordpunct_tokenize(x) for x in messages)).most_common(10))
    error_tokens = {}
    for word, count in array:
        error_tokens[word] = count
    
    error_messages_tokens[key] = error_tokens

# Write error messages token dict to a file
with open('./log/log_analysis_tokens.json', 'w') as fp:
    json.dump(error_messages_tokens, fp, indent=4)