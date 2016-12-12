shopping_list = []
while True:
    item=input("Insert new item, press enter when shopping is done ")
    if not item:
        break
    else:
        shopping_list.append(item)
print ("The list is ",shopping_list)
