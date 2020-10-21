import sys
import os

if sys.platform.lower() == "win32":
    os.system('color')

black = lambda x: '\033[30m' + str(x)+'\033[0;39m'
red = lambda x: '\033[31m' + str(x)+'\033[0;39m'
green = lambda x: '\033[32m' + str(x)+'\033[0;39m'
yellow = lambda x: '\033[33m' + str(x)+'\033[0;39m'
blue = lambda x: '\033[34m' + str(x)+'\033[0;39m'
magenta = lambda x: '\033[35m' + str(x)+'\033[0;39m'
cyan = lambda x: '\033[36m' + str(x)+'\033[0;39m'
white = lambda x: '\033[37m' + str(x)+'\033[0;39m'
