from shell_command import ShCommand

import logging
import os

path = '../dts-generate-results/results/4_extract-code/code'
packages = os.listdir(path)
print(" Number of packages to be installed: " + str(len(packages)))
# Configuring logger
logging.basicConfig()
logger = logging.getLogger()


for package in packages:
    # Creating an empty npm-modules sub directory
    mkdir_cmd = "mkdir -p " + path + "/" + package + "/node_modules"
    ShCommand(mkdir_cmd, logger, "mkdir", 3600).run()
    npm_install_cmd = "npm install --prefix " + path + "/" + package + " " + package
    ShCommand(npm_install_cmd, logger, "npm-installer", 3600).run()