#Trip problem(P-2)
print('Enter number of persons')
a=int(input())
amount=[]
print('Enter their respective amount')
for i in range(0,a):
    amount.append(float(input()))
avg=sum(amount)/a
exchange=0
exchange1=0
exchange2=0
exchange3=0
for i in range(0,a):
    if amount[i]<avg:
        exchange1+=avg-amount[i]
    elif amount[i]>avg:
        exchange2+=amount[i]-avg
    elif amount[i]==avg:
        exchange3=0
exchange=exchange1+exchange2+exchange3
print(exchange/2)
