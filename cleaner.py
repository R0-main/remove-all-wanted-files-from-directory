from ast import Tuple
from os import listdir, remove
from os.path import isfile, join


class Cleaner :

    def __init__(self, path : str, entensions : Tuple[str, ...]):
        self.entensions = entensions 
        self.path = path 

    def run(self):
        print("starts script...")
        self.deleteFromPath(self.path)

    def deleteFromPath(self, path):
        print(f"deleting files in {path}...")
        for file in listdir(path):
            if isfile(join(path, file)) :
                if file.endswith(self.entensions):
                    remove(file)
            else :
                self.deleteFromPath(file)
