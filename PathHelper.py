import os

def getMainSubfolder(folder):
    return os.path.join(getMainFolder(), folder)

def getMainFolder():
    return os.path.dirname(os.getcwd())

def getOutputPath(filename=None):
    return os.path.join(getMainSubfolder('outputs'), filename)

def getLogPath(filename=None):
    return os.path.join(getMainSubfolder('logs'), filename)

def getInputPath(filename=None):
    return os.path.join(getMainSubfolder('inputs'), filename)

def getConfigPath(filename=None):
    return os.path.join(getMainSubfolder('configs'), filename)

# def getAppDirectoryPath():
#     return os.getcwd()

# def getCorePath():
#     return os.path.dirname(os.path.abspath(__file__))