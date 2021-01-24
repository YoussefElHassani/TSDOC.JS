from shell_command import ShCommand 
from fnmatch import fnmatch
from pathlib import Path

import subprocess
import logging
import sys
import os

# Configuring logger
logging.basicConfig(filename='./log/analysis.log')
logger = logging.getLogger()

# including Jalangi input
jalangi_path = "../jalangi2/src/js/commands/jalangi.js"
analysis_path = "src/js/error_analysis.js"
# source files root folder
root = '../test-code'
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
filtered_paths = [i for i in filtered_paths if 'babel' not in i]
print("Filtering - DONE")
print("Total files to be processed: " + str(len(filtered_paths)))

# Running jalangi
for source_path in filtered_paths:
    # Downgrading the javascript version to ES5 using babbel
    babel_command = "npx babel " + source_path + " --out-file " + source_path
    # Convert javascript to the latest
    ShCommand(babel_command, logger, "Shell_Runner", 30).run()
    # Executing the analysis on the downgraded script
    run_command_babel = "node --no-deprecation " + jalangi_path + " --analysis " + analysis_path + " " + source_path
    # Fork a new thread to instrument the babel converted code using jalangi
    ShCommand(run_command_babel, logger, "Shell_Runner", 30).run()

print('Analysis complete!')

# node --no-deprecation ../jalangi2/src/js/commands/jalangi.js + source_path