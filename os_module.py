import os

os.chdir("h:/")
files = os.listdir()
files.pop(0)
# print(files)

for file in files :
    os.remove(file)
