#Trip Problem
print('Enter number of persons')
a=int(input())
print('Enter their amount')
amount=[]
for i in range(0,a):
    amount.append(float(input()))
avg=sum(amount)/a
share1=0
share2=0
for i in range(0,a):
    if amount[i]<avg:
        share1=(avg-amount[i])
    elif amount[i]>=avg:
        share2=amount[i]-avg
if share1<share2:
    print(share1)
else:
    print(share2)
