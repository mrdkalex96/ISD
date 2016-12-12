class Person():
    def __init__(self,name = "unknown"):   #name already given in the parameters
        self._name = name

        
    def printName(self):
        print (self._name)

p = Person()
p.printName()
