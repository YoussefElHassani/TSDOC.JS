import os
import pandas as pd
import re
import regex
import json
import ast 



pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
data = []
path = './log/info.log'
file_ = open(path, "r")
lines = file_.read()
print(len(lines))

patterns = pattern.findall(lines)
for pattern in patterns:
    pattern = ast.literal_eval(pattern) 
    print(pattern)