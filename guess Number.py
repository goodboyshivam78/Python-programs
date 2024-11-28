import random

print("HARE KRISHNA to all +_+\n")
print("1 se 20 ke bich me maine ek number socha hai !_!")
guess = random.randint(1,20)
my_guess = ''
count = 0
while True:
    count +=1
    my_guess = int(input("Wo kon sa number hai..Batiye ?\n"))
    if my_guess > guess:
        print("Aaa kuch jada hi soch liya +_+!")
    elif my_guess < guess :
        print("Apne kuch kam socha hai -_-!")
    else:
        print("Maan gaye, aapne bilkul sahi socha ",guess)
        break

print("Aapne "+str(count)+" baar me sahi soch, Accha khela aapne *_*")
