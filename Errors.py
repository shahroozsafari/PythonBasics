
# for i in range(100) :
#     print(i)

while True :
    try :
        a = float(input("skjdhdkjasdkas :"))
        b=5/a
    except (ValueError, NameError) as err :
        print("Wrong Data ! Try again ...")
        print(err)
    except (ZeroDivisionError) as err :
        print("The number MUST be a none zero value .")
        print(err)
    else :
        print(b)
        break
    finally :
        print("===============")
