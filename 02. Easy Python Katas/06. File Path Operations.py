class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath

    def extension(self):
        return self.filepath[self.filepath.rfind(".")+1:]

    def filename(self):
        return self.filepath[self.filepath.rfind("/")+1:self.filepath.rfind(".")]

    def dirpath(self):
        return self.filepath[:self.filepath.rfind("/")+1]


master = FileMaster('/Users/person1/Pictures/house.png')
print(master.extension())
print(master.filename())
print(master.dirpath())