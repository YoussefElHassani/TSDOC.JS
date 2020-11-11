import os
import pandas as pd
import re
import regex
import json


pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
data = []
path = './log/info.log'
file_ = open(path, "r")
lines = file_.read()
print(len(lines))

patterns = pattern.findall(lines)
for pattern in patterns:
    json_dict= json.loads(pattern)
    print(pattern)
#for line in lines:
#data.append(myfile.read())

#df = pd.DataFrame(data)

#print(df)