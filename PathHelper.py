import os

def getMainSubfolder(folder):
    return os.path.join(getMainFolder(), folder)

def getMainFolder():
    return os.path.dirname(os.getcwd())

def getOutputPath(filename=None):
<<<<<<< HEAD
    if filename == None:
        return getMainSubfolder('outputs')
    else:
        return os.path.join(getMainSubfolder('outputs'), filename)
=======
    folder_name = 'outputs'
    if filename==None:
        return getMainSubfolder(folder_name)
    else:    
        return os.path.join(getMainSubfolder(folder_name), filename)
>>>>>>> a615f2d858b9add8c9ade6d92cb57db29b882aec

def getLogPath(filename=None):
    folder_name = 'logs'
    if filename==None:
        return getMainSubfolder(folder_name)
    else:    
        return os.path.join(getMainSubfolder(folder_name), filename)

def getInputPath(filename=None):
<<<<<<< HEAD
    if filename == None:
        return getMainSubfolder('inputs')
    else:
        return os.path.join(getMainSubfolder('inputs'), filename)   
=======
    folder_name = 'inputs'
    if filename==None:
        return getMainSubfolder(folder_name)
    else:    
        return os.path.join(getMainSubfolder(folder_name), filename)
>>>>>>> a615f2d858b9add8c9ade6d92cb57db29b882aec

def getConfigPath(filename=None):
    folder_name = 'configs'
    if filename==None:
        return getMainSubfolder(folder_name)
    else:    
        return os.path.join(getMainSubfolder(folder_name), filename)
# def getAppDirectoryPath():
#     return os.getcwd()

# def getCorePath():
#     return os.path.dirname(os.path.abspath(__file__))