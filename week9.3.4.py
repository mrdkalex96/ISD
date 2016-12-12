class CashRegister :
# Comment 1
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      self._change = 0.0
   # Comment 2
   def addItem(self, price) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price 
      
   # Comment 3
   def getTotal(self) :
      return self._totalPrice
      
   # Comment 4
   def getCount(self) :
      return self._itemCount
      print (self._itemCount)
   # Comment 5
   def clear(self):
      self._itemCount = 0
      self._totalPrice = 0.0

   def getPounds(self,):
      return round(self._totalPrice,0)
      
   def giveChange(self,payment):
      self._payment = payment
      self._change = self._payment - self._totalPrice
      return self._change
      

register1 =CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)
register2 = CashRegister()
register2.addItem(1.90)
register2.giveChange(50)
register2.getPounds()

print(register1._itemCount)
print(register1._totalPrice)
print(register2._itemCount)
print(register2._totalPrice)
print("The price in pound is",register2.getPounds())
print("The change is",register2.giveChange(50),"£")








