class CashRegister :
# Comment 1: initialising the class with two objects itemCount and totalPrice
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      
# Comment 2: definition of a behavior of the class
#which adds the price and count of one item
   def addItem(self, price) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price 
      
# Comment 3: definition of getTotal which returns the totalPrice
   def getTotal(self) :
      return self._totalPrice
      
# Comment 4: definition of getCount, which returns the item count and prints it
   def getCount(self) :
      return self._itemCount
      print (self._itemCount)
      
# Comment 5: definition of clear which clears all the transactions
#from the register
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      
# function getPound which rounds the total price
   def getPounds(self):
      return round(self._totalPrice,0)


   # function giveChange which calculates the change for the customer      
   def giveChange(self,payment):
      self._payment = payment
      self._change = self._payment - self._totalPrice
      return self._change


register1 =CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)
register2 = CashRegister()
register2.addItem(1.90)
register2.getPounds()
register2.giveChange(50)


print (register1._itemCount)
print (register1._totalPrice)
print (register2._itemCount)
print (register2._totalPrice)
print("The price in pound is",register2.getPounds())
print("The change is",register2.giveChange(50),"£")
