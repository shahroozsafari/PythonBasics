import matplotlib.pyplot as plt

year =["1398","1399","1400","1401","1402"]
product = [500,600,350,300,700]


plt.plot(year,product)
plt.show()

plt.bar(year,product,color="red")
plt.show()