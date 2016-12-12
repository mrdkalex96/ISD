class Person():      
    def __init__(self,firstName):  
        self._name = firstName  
 
    def printName(self):    #prints the name
        print(self._name)

harry = Person("Harry")  #creating the object "Harry" from the class Person
harry.printName()
