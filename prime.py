
number = int(input("Enter your number : "))
for i in range(2,int(number**0.5)+1) :
    if number % i == 0 :
        input("Your number IS NOT prime!")
        break
else:
    input("Your number IS prime.")
