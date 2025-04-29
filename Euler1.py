
total = 0
for i in range(3,1000):
    if i%3==0 or i%5==0 :
        total = total + i 
print("Sumation =",total)


numbers=[]
for i in range(3,1000) :
    if i%3==0 or i%5==0 :
        numbers.append(i)
print(sum(numbers))


numbers.sort()
print(max(numbers))
