num= int(input("Enter Number: "))
if num==0 or num==1:
    k=1
for i in range(2,num+1):
    if num % i == 0:
        k=1
    else:
        k=0
if k==1:
    print("Number is not a prime Number")
else:
    print("Number is a prime number")