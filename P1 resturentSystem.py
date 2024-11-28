
print("---------------------------------------WELCOME TO LILY RESTAURENT *_* --------------------------------------\n")
menue = {"coffee":"Rs30","tea":"Rs20","maggie":"Rs40","noodles":"Rs60","samosha":"Rs10","burger":"Rs50","pizza":"Rs129","pasta":"Rs100","sandwich":"Rs80","coldrink":"Rs20"}
for i, j in menue.items():
    print(i.capitalize(),":",j)
print("------------------------------------------------------------------------------------------------------------")
check = "y"
orderList = []
while check=="y" :
    order = list(map(str, input("Enter the items you want to order:").split()))
    orderList.extend(order)
    check = input("Do you want to order more items (y/n):")
bill = []
print("-------------------------------\n")
for i in orderList:
    if i.lower() in menue:
        print(f"{i} :      {menue[i.lower()]}")
        bill.append(int(menue[i.lower()][2:]))
    else:
        print(f"'{i}' is not available!")
print("-------------------------------")
print(f"Your total bill is: Rs {sum(bill)}/-")
