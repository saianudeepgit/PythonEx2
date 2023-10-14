import os
os.mkdir("Exceptionsprint.txt","w")
f=open("Exceptionsprint.txt","r")
while(True):
    itemName = input("enter the item name :")
    itemid = input("enter the item id:")
    itemid.isdigit
    itemQty = int(input("the no of items available:"))
    itemPrice = float(input("enterthe price of the item:"))
    nextitem = input("do you want to enter new record: Y/N")
    if(nextitem == 'Y' or nextitem == 'y'):
        print(itemid,itemName,itemQty,itemPrice,nextitem)
        continue
    else:
        break
f.close()