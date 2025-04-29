

def calc(a,b,c,d=1)  :
    result = (a+b+c)*d
    return result

def average(x,y,z) :
    return round((x+y+z)/3,2)
            
def concat(a,b,c,d) :
    return a+b+c*d


def mean(n,*numbers) :
    return round((sum(numbers)+n) / (len(numbers)+1) ,2)

def kala(**features) :
    for f in features.items() :
        print(f)

average = lambda x,y,z : round((x+y+z)/3 ,2)


#-------------- Main ----------------


# print(calc(4,7,9))
# print(average(7.3,11.5,18.2))
# print(mean(5,7,9,8,10))
# kala(type="tv",brand="Samsung",size=50,price=1600,weight=7.5)
