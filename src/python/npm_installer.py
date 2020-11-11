from shell_command import ShCommand

import logging
import os

path = '../dts-generate-results/results/4_extract-code/code/'
packages = os.listdir(path)

# Configuring logger
logging.basicConfig()
logger = logging.getLogger()

for package in packages:
    command = "npm install " + package
    ShCommand(command, logger, "npm-installer", 3600).run()