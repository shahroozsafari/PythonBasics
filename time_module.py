
from time import sleep, time
# print(time.time())          # Epoch Time  1970/01/01  

start  = time()
for i in range(1000) :
    print(i)
end = time()

print(end-start)

sleep(3)
print("-------------------")