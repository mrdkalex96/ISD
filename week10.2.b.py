from cashRegister import CashRegister

def main():
    register1 = CashRegister()   
    register1.addItem(3)
    register1.addItem(4)
    print(register1.getCount())  # testing addItem and getCount
    print(register1.getTotal())  # testing getTotal
    print(register1.giveChange(50)) # testing giveChange
    
main()
