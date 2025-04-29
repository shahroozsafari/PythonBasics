
def prn(number) :
    print(number)

a=100
b=200
c=300
for i in range(20) :
    n=a+b+c+(i**2)
    print(i)
    if n>700 :
        prn(n)
        print("===================")
        break
print("****************")