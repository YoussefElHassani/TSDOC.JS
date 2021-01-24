from fnmatch import fnmatch
from shell_command import ShCommand

import subprocess
import logging
import os
import re

# Configuring logger
logging.basicConfig()
logger = logging.getLogger()

# including Jalangi input
jalangi_path = "../jalangi2/src/js/commands/jalangi.js"
analysis_path = "src/js/error_analysis_babel.js"

# source files root folder
root = '../test-code'

# javascript pattern
pattern_js = "*.js"

# Os walk to find all js files
print("Fetching code examples...")
all_scripts_path = []
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern_js):
            all_scripts_path.append(os.path.join(path, name))

# Pattern for parsing the npm modules required within the JS files
print("Parsing NPM imports...")
npm_packages = {}
for path in all_scripts_path:
    dir_name = os.path.dirname(path)
    
    if dir_name not in npm_packages:
        npm_packages[dir_name] = []
    for line in open(path):
        match = re.search('require(.*)', line)
        if match:
            npm_package = str(re.findall(r"['\"](.*?)['\"]", match.group(0)))
            npm_packages[dir_name].append(npm_package.strip("[\'\']"))
            
# Install the npm modules
print("Installing NPM modules")
for directory, npm_package_list in npm_packages.items():
    mkdir_cmd = "mkdir -p " + directory + "/node_modules"
    for npm_package in npm_package_list:
        # Creating an empty npm-modules sub directory
        mkdir_cmd = "mkdir -p " + directory +"/node_modules"
        ShCommand(mkdir_cmd, logger, "mkdir", 3600).run()
        npm_install_cmd = "npm install --prefix " + directory + " " + npm_package
        ShCommand(npm_install_cmd, logger, "npm-installer", 3600).run()
print("Installation done")
