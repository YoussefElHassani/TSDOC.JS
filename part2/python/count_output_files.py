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
    os.rename(file_path[:-3]+"_jalangi_.js", file_path)
    #os.remove(file_path[:-3]+"_jalangi_.json")
    #os.remove(file_path)


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
    """if module not in test:
        continue"""
    
    # git clone
    logging.info("Cloning file: " + git_link + " into: " + github_repositories_path + module)
    git_command = "git clone git://" + git_link + ' '+ github_repositories_path + module
    ShCommand(git_command, logger, "Shell_Runner", 3600).run()
    # check if test file exists and contains .js files