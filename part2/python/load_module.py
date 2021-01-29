from shell_command import ShCommand 
from fnmatch import fnmatch
from shutil import copy2


import logging
import csv
import os

def fetch_js_files(root):
    all_files = []
    pattern = "*.js"

    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                all_files.append(os.path.join(path, name))
    # Adding filters    
    filtered_paths = [i for i in all_files if 'node_modules' not in i]

    return filtered_paths

def refactor_jalangi(file_path):
    os.remove(file_path)
    os.remove(file_path[:-3]+"_jalangi_.json")
    os.rename(file_path[:-3]+"_jalangi_.js", file_path)

def inject_jalangi(file_path, root):
    module = os.path.abspath(root+ "/jalangi_addon.js")
    with open(file_path, 'r') as original: data = original.read()
    with open(file_path, 'w') as modified: modified.write("var J$ = require(\'" +module+ "\');\n" + data)

##################################################
test = ['amazon-product-api', 'amqp-connection-manager', 'align-text', 'ali-oss', 'archiver', 'apicache', 'ajv-errors', 'algoliasearch', 'aqb', 'algebra.js', 'amqp', 'arcgis-to-geojson-utils', 'appdmg', 'antlr4-autosuggest', 'algoliasearch-helper', 'ansi-escape-sequences', 'any-db', 'angular-load', 'anymatch', 'alexa-voice-service', 'amqplib', 'app-module-path', 'angular-spinner', 'ajv-merge-patch', 'app-root-dir', 'agent-base', 'api-error-handler', 'amplify', 'ansi-colors', 'angular-bootstrap-calendar', 'animejs', 'amazon-cognito-auth-js', 'ansicolors', 'alt', 'almost-equal', 'are-we-there-yet']
###################################################

# Configuring logger
logging.basicConfig(filename='./log/analysis.log', level=logging.DEBUG)
logger = logging.getLogger()

logging.info('New execution --')
# including Jalangi command and add-om
jalangi_addon = './util/jalangi_addon.js'
jalangi_command_path = "../jalangi2/src/js/commands/jalangi.js"

# get packages names and github repository link
npm_modules_path = "./util/modules.csv"

# Github repositories path
github_repositories_path = "../test-repos/"

# Extracting the github link from the modules.csv file
with open(npm_modules_path, mode='r') as infile:
    reader = csv.reader(infile)
    npm_modules = {rows[0]:rows[1] for rows in reader}

npm_modules = {k: v for k, v in npm_modules.items() if len(v) >= 10}

for (count,(module, git_link)) in enumerate(npm_modules.items()):
    if module not in test:
        continue
    
    # git clone
    logging.info("Cloning file: " + git_link + " into: " + github_repositories_path + module)
    git_command = "git clone https://" + git_link + ' '+ github_repositories_path + module
    ShCommand(git_command, logger, "Shell_Runner", 3600).run()
    # check if test file exists and contains .js files
    
    # npm install
    logging.info("Installing npm packages in: " + github_repositories_path + module)
    npm_install = "npm -prefix " + github_repositories_path + module + " install"
    ShCommand(npm_install, logger, "Shell_Runner", 3600).run()
    
    logging.info("Extracting all .js files from: " + github_repositories_path + module)
    js_files = fetch_js_files(github_repositories_path + module)
    for file_ in js_files:
        # babel
        logging.info("Converting file to ES5: " + file_)
        babel_command = "npx babel " + file_ + " --out-file " + file_
        # Convert javascript to the latest
        ShCommand(babel_command, logger, "Shell_Runner", 30).run()
        
        # Jalangi
        logging.info("Instrumenting file using Jalangi2: " + file_)
        jalangi_command = "node --no-deprecation " + jalangi_command_path + " " + file_
        # Fork a new thread to instrument the babel converted code using jalangi
        ShCommand(jalangi_command, logger, "Shell_Runner", 30).run()
        refactor_jalangi(file_)
        inject_jalangi(file_, github_repositories_path + module)
        
    # Copy the jalangi add_on into the new repositories
    copy2(jalangi_addon, github_repositories_path + module)
    
    # TODO: Remove Linters because they fail tests
    
    # Execute npm test
    npm_install = "npm -prefix " + github_repositories_path + module + " test"
    ShCommand(npm_install, logger, "Shell_Runner", 3600).run()
    # TODO: run example files


