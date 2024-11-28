def findEmail(tect):
    x = list(tect.split())
    y = [i for i in x if i.endswith("@gmail.com")]
    for i in y:
        print(f"Email deceted : {i}")


text ="this is my first gmail shivamsingh78@gmail.com and this is my second email skingofkings78@gmail.com"
findEmail(text)
print("Done")