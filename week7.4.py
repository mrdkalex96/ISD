def isLeftSidePage():
    page = int(input("Insert the page number: "))
    if page %2 == 0:
        print(page)
        return True
        
    else:
        print("%60s%d" % (" ", page))
        return False

               
print(isLeftSidePage())
