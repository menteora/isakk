import os

class PathHelper:
    def __init__(self, path=None):
        if path is None:
            self.path = None
        else:
            self.path = path

    def setBasePath(path):
        self.path = path

    def getMainSubfolder(self, folder):
        return os.path.join(self.getMainFolder(), folder)

    def getMainFolder(self):
        if self.path is not None:
            base_path = self.path
        else:
            base_path = os.path.dirname(os.getcwd())
        return base_path

    def getOutputPath(self, filename=None):
        folder_name = 'outputs'
        if filename==None:
            return self.getMainSubfolder(folder_name)
        else:    
            return os.path.join(self.getMainSubfolder(folder_name), filename)

    def getLogPath(self, filename=None):
        folder_name = 'logs'
        if filename==None:
            return self.getMainSubfolder(folder_name)
        else:    
            return os.path.join(self.getMainSubfolder(folder_name), filename)

    def getInputPath(self, filename=None):
        folder_name = 'inputs'
        if filename==None:
            return self.getMainSubfolder(folder_name)
        else:    
            return os.path.join(self.getMainSubfolder(folder_name), filename)

    def getConfigPath(self, filename=None):
        folder_name = 'configs'
        if filename==None:
            return self.getMainSubfolder(folder_name)
        else:    
            return os.path.join(self.getMainSubfolder(folder_name), filename)

    def getBinPath(self, filename=None):
        folder_name = 'configs'
        if filename==None:
            return self.getMainSubfolder(folder_name)
        else:    
            return os.path.join(self.getMainSubfolder(folder_name), filename)
# def getAppDirectoryPath():
#     return os.getcwd()

# def getCorePath():
#     return os.path.dirname(os.path.abspath(__file__))