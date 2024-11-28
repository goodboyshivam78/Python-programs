def isPhoneNumber(num):
    if len(num) != 12 or (not (num[:3].isdecimal() or num[4:7].isdecimal() or num[8:].isdecimal() )) or (num[3]+num[7] != '--') :
        return False
    else:
        return True
    
text = "This is my offic number 773999-3283 and this is my collage number 728-295-3361"
for i in range(len(text)):
    chunk = text[i:i+12]
    if isPhoneNumber(chunk):
        print(f"Phone number dectected: {chunk}")   
print("Done")
    