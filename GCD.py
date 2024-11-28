
def HCF(n1,n2):
    GCD = 1
    if n1<=n2:
        for i in range(2,n1+1):
            if n1%i==0 and n2%i==0 :
                GCD = i
    else :
        for i in range(2,n2+1):
            if n1%i==0 and n2%i==0 :
                GCD = i  
    return GCD

n = int(input("Enter n1:"))
m = int(input("Enter n2:"))
Answer  = HCF(n,m)
print(f"HCF Of {n}, {m} is: {Answer}")

