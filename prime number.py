print("---------------------Hare Krishna-----------------------\n")
n = int(input("Enter a number : "))
m=0
if (n<2) :
    print(f"{n} Is not a prime number !")
elif (n==2):
    print(f"{n} Is prime Number")
else : 
    for i in range(2,n) :
        if (n%i==0) :
            m=1
    if (m==0):
        print(f"{n} Is prime Number")
    else:
        print(f"{n} Is not a prime number !")