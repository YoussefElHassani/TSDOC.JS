from shell_command import ShCommand 

import logging
import csv


# Configuring logger
logging.basicConfig(filename='./log/analysis.log')
logger = logging.getLogger()

# including Jalangi command and add-om
jalangi_addon = './util/jalangi_addon.js'
jalangi_command_path = "../jalangi2/src/js/commands/jalangi.js"

# get packages names and github repository link
npm_modules_path = "./util/modules.csv"

# Extracting the github link from the modules.csv file

with open(npm_modules_path, mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}

print(mydict)
# Github repositories path
github_repositories_path = "../test-repos/"

