import os

def getMainSubfolder(folder):
    return os.path.join(getMainFolder(), folder)

def getMainFolder():
    return os.getcwd()

def getOutputPath(filename=None):
    folder_name = 'outputs'
    if filename==None:
        return getMainSubfolder(folder_name)
    else:    
        return os.path.join(getMainSubfolder(folder_name), filename)

def getLogPath(filename=None):
    folder_name = 'logs'
    if filename==None:
        return getMainSubfolder(folder_name)
    else:    
        return os.path.join(getMainSubfolder(folder_name), filename)

def getInputPath(filename=None):
    folder_name = 'inputs'
    if filename==None:
        return getMainSubfolder(folder_name)
    else:    
        return os.path.join(getMainSubfolder(folder_name), filename)

def getConfigPath(filename=None):
    folder_name = 'configs'
    if filename==None:
        return getMainSubfolder(folder_name)
    else:    
        return os.path.join(getMainSubfolder(folder_name), filename)
    
def getBinPath(filename=None):
    folder_name = 'bin'
    if filename==None:
        return getMainSubfolder(folder_name)
    else:    
        return os.path.join(getMainSubfolder(folder_name), filename)

# def getAppDirectoryPath():
#     return os.getcwd()

# def getCorePath():
#     return os.path.dirname(os.path.abspath(__file__))