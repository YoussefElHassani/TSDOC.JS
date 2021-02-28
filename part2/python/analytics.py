# Finding how many runtime information files were generated
import os
from fnmatch import fnmatch

pattern = "output.json"
root = "../runtime_information_files/"

print("Fetching code examples...")
all_scripts_path = []
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            all_scripts_path.append(os.path.join(path, name))

#for file_ in all_scripts_path:
#    print(file_)
    
print(len(all_scripts_path))