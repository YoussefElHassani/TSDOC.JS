from shell_command import ShCommand 
from fnmatch import fnmatch
from shutil import copy2
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool


import logging
import shutil
import json
import csv
import os

def updateJsonFile(root):
    jsonFile = open(root + "/package.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    ## Working with buffered content
    data["scripts"]["pretest"] = ""
    data["scripts"]["test"] = data["scripts"]["test"].replace('&&', ';')

    ## Save our changes to JSON file
    jsonFile = open(root + "/package.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

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
    try:
        os.rename(file_path[:-3]+"_jalangi_.js", file_path)
        os.remove(file_path[:-3]+"_jalangi_.json")
    except:
        return


def inject_jalangi(file_path, root):
    with open(file_path, 'r') as original: data = original.read()
    
    if root in file_path:
        temp = file_path.replace(root,'')
        temp = temp[1:]

    directory_count = temp.count('/')
    jalangi_addon_path = ""
    
    if(directory_count == 0):
        jalangi_addon_path += './'
    else:
        for i in range(directory_count):
            jalangi_addon_path += '../'
    jalangi_addon_path += 'jalangi_addon.js'

    with open(file_path, 'w') as modified: modified.write("var J$ = require(\'" + jalangi_addon_path + "\');\n" + data)


def process_javascript_file(file_, module):
    # babel
    logging.info("Converting file to ES5: " + file_)
    babel_command = "npx babel " + file_ + " --out-file " + file_
    
    # Convert javascript to the latest
    ShCommand(babel_command, logger, "Shell_Runner", 120).run()
    
    # Jalangi
    logging.info("Instrumenting file using Jalangi2: " + file_)
    jalangi_command = "node --no-deprecation " + jalangi_command_path + " " + file_
    
    # Fork a new thread to instrument the babel converted code using jalangi
    ShCommand(jalangi_command, logger, "Shell_Runner", 120).run()
    refactor_jalangi(file_)

    inject_jalangi(file_, github_repositories_path + module)

def generate_runtime_files( module, git_link):
    github_repositories_path = "../test-repos/"
    try:
        print("processing: " + module)        
        # git clone
        logging.info("Cloning file: " + git_link + " into: " + github_repositories_path + module)
        git_command = "git clone https://" + git_link + ' '+ github_repositories_path + module
        ShCommand(git_command, logger, "Shell_Runner", 1200).run()
        # check if test file exists and contains .js files
        if len(os.listdir(github_repositories_path + module)) > 100:
            shutil.rmtree(github_repositories_path + module)
            print("SKIPPED: Module")
            return
        # npm install
        logging.info("Installing npm packages in: " + github_repositories_path + module)
        npm_install = "npm -prefix " + github_repositories_path + module + " install"
        ShCommand(npm_install, logger, "Shell_Runner", 3600).run()
        
        logging.info("Extracting all .js files from: " + github_repositories_path + module)
        js_files = fetch_js_files(github_repositories_path + module)
        
        # Copy the jalangi add_on into the new repositories
        copy2(jalangi_addon, github_repositories_path + module)
        
        # Tranform javascript file to ES5 and instrument using Jalangi
        for js_file in js_files:
            process_javascript_file(js_file, module)
        
        # mkdir for output file
        runtime_info_path = "../runtime_information_files/" + module
        os.mkdir(runtime_info_path)
        
        # Escape linters
        updateJsonFile(github_repositories_path + module)
        
        # Execute npm test
        npm_install = "npm -prefix " + github_repositories_path + module + " test"
        ShCommand(npm_install, logger, "Shell_Runner", 3600).run()
        print("DONE: " + module)
    except:
        logging.info("Installing npm packages in: " + github_repositories_path + module)
        print("TERMINATED:" + module)
        return

def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders


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
npm_modules = {k: v for k, v in npm_modules.items() if len(v) >= 10 and ('lodash' not in k)}



# Remove this later
# npm_modules = {"html-tag-names": "github.com/wooorm/html-tag-names"}

# Remove already processed files
processed_files = [x.split('/')[-1] for x in fast_scandir("../runtime_information_files/")]
print(len(npm_modules))

npm_modules =  {k: v for k, v in npm_modules.items()if k not in processed_files}

# Remove this later
#npm_modules = {"abs": "github.com/IonicaBizau/abs"}
print(len(npm_modules))
# Convert npm modules dict to a tuples list
npm_modules = list(npm_modules.items())
# Pass the list to the pool
pool = Pool()
pool.starmap(generate_runtime_files, npm_modules)

