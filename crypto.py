#Cryptography
string="Hello Folks"
value=int(input("Enter the value by which you want to increment it:"))
cryp_string=""
for i in range(0, len(string)):
    if string[i]!=" ":
        cryp_string+=chr(ord(string[i])+value)
    else:
        cryp_string+=" "
print(cryp_string)
