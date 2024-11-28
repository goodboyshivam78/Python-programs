def LCM(n,m) :
    lcm = 1
    if m>=n:
        for i in range(n*m,m+1,-1):
            if i%n==0 and i%m==0:
                lcm = i
                print("Radhe Radhe")
    else:
        for i in range(n*m,n+1,-1):
            if i%n==0 and i%m==0:
                lcm = i
    return lcm

n = int(input("Enter n1: "))
m = int(input("Enter n1: "))
ans = LCM(n,m)
print(f"The LCM of {n},{m} is: {ans}")