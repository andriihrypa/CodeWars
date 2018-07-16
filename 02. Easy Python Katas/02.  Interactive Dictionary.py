#www.codewars.com/kata/interactive-dictionary/train/python


class Dictionary():
    def __init__(self):
        self.dict = {}


    def newentry(self, word, definition):
        self.dict[word] = definition

    def look(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return "Can't find entry for " + key


d = Dictionary()
d.newentry("Apple", "A fruit")

print(d.look("Apple"))