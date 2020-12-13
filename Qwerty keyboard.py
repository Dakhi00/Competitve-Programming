#Qwerty Keyboard
dict1={'W':'Q','E':'W','R':'E','T':'R','Y':'T','U':'Y','I':'U','O':'I','P':'O','[':'P','S':'A','D':'S','F':'D','G':'F','H':'G','J':'H','K':'J','L':'K',';':'L','X':'Z','C':'X','V':'C','B':'V','N':'B','M':'N',',':'M','.':',','/':'.'}
print('Enter string')
string=input()
Final=""
for i in string:
    if i==" ":
        Final+=" "
    else:
        Final+=dict1[i]
print(Final)
