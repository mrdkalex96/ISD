class CashRegister :
   
   def __init__(self,itemCount=0,totalPrice=0.0):
      self._itemCount = itemCount
      self._totalPrice = totalPrice
      
   
   def addItem(self, price) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price 
      
   
   def getTotal(self) :
      return self._totalPrice

   def getCount(self) :
      return self._itemCount

   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0

   def giveChange(self,payment):
       self._payment = payment
       self._change = self._payment - self._totalPrice
       return self._change

   
