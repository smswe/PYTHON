#Counting of 5 Fingers
n=int(input("Enter the Count: "))
r=n%8
if r==0:
    print(2)
elif r<5:
    print(r)
elif r>5:
    print(10-r)

#Counting of 10 Fingers
n=int(input("Enter the Count: "))
r=n%18
if r==0:
    print(2)
elif r<10:
    print(r)
elif r>10:
    print(20-r)
