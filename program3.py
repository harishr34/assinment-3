#WAP to find the total number of people above the age of 18
d={ "harish":20,
    "adi":19,
    "nagu":13,
    "gaja":28,
    "santhosh":31,
    "naveen":15,
    "halappa":25,
    "kiran":30,}
print(d)
l=d.values()
e=[]
for i in l:
    if i>18:
        e.append(i)
n=len(e)
print('number of peoples,age above 18:-',n)