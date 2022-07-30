n=int(input("Enter Number:"))
x=n+1
flag=0
for i in range (1,x):
    if i*i == x:
        flag=1
        break
if flag ==1:
    print("sunny numner")
else:
    print("Not a Sunny Number")
