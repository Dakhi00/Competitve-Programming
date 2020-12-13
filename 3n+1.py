a=int(input("Enter number"))
b=1
while(a>1):
    if(a%2==0):
        a=a/2
        b=b+1
    else:
        a=3*(a)+1
        b=b+1
print(b)
