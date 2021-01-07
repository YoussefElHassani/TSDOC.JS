from shell_command import ShCommand 
from fnmatch import fnmatch

import subprocess
import logging
import sys
import os

# Configuring logger
logging.basicConfig()
logger = logging.getLogger()

# including Jalangi input
jalangi_path = "../jalangi2/src/js/commands/jalangi.js"
analysis_path = "src/js/error_analysis_babel.js"

# source files root folder
root = '../dts-generate-results/results/4_extract-code/code'
#root = '../dts-generate-results/results/test'

pattern = "*.js"

print("Fetching code examples...")
all_scripts_path = []
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            all_scripts_path.append(os.path.join(path, name))
print("Code examples fetched!")

# Removing files that contain "jalangi"
filtered_paths = [i for i in all_scripts_path if 'node_modules' not in i]
filtered_paths = [i for i in filtered_paths if 'jalangi' not in i]
print("Filtering - DONE")

# Running jalangi
for source_path in filtered_paths:
    # First, we creater the babel converted destination path
    substr = ".js"
    inserttxt = "_babel"

    babel_source_path = source_path.replace(substr, inserttxt + substr)
    
    # Downgrading the javascript version to ES5 using babbel
    babel_command = "npx babel " + source_path + " --out-file " + babel_source_path
    ShCommand(babel_command, logger, "Shell_Runner", 10).run()
    # Executing the analysis on the downgraded script
    command = "node --no-deprecation " + jalangi_path + " --inlineIID --inlineSource --analysis " + analysis_path + " " + babel_source_path
    ShCommand(command, logger, "Shell_Runner", 10).run()
