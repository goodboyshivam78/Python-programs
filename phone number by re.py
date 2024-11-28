import re

reObj  = re.compile(r'\d{3}-\d{3}-\d{4}')
number = reObj.search("Hello my number is 123-765-9268 and my friend number is 974-843-8547")
print("\nThe phone numbrs are: ",number.group())


# We make groups in side the regix pattern using () as:- re.compile(r'(\d{3})-(\d{3}-\d{4})') and we use groups in place of group
reObj  = re.compile(r'(\d{3})-(\d{3}-\d{4})')
number = reObj.search("Hello my number is 123-765-9268 and my friend number is 974-843-8547")
print("\nThe phone numbrs are: ",number.group(1))
print("The phone numbrs are: ",number.groups())


# we use findall() in place of search() to match one or more rigex pattern from the given text.
reObj  = re.compile(r'\d{3}-\d{3}-\d{4}')
number = reObj.findall("Hello my number is 123-765-9268 and my friend number is 974-843-8547")
print("\n",number)
print("The phone numbrs are: ", ', '.join(number))


# we use groups in side regix pattern and use findall()
reObj  = re.compile(r'(\d{3})-(\d{3}-\d{4})')
number = reObj.findall("Hello my number is 123-765-9268 and my friend number is 974-843-8547")

print("\nThe phone numbrs are: ", number)
