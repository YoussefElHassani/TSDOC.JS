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
analysis_path = "src/js/error_analysis.js"

# source files root folder
root = '../dts-generate-results/results/4_extract-code/code/'
pattern = "*.js"

all_scripts_path = []
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            all_scripts_path.append(os.path.join(path, name))


for source_path in all_scripts_path:
    command = "node --no-deprecation " + jalangi_path + " --inlineIID --inlineSource --analysis " + analysis_path + " "+ source_path
    ShCommand(command, logger, "Shell_Runner", 10).run()
