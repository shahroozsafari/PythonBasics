
with open("d:/mydata.txt","r+") as data :
    data.write("Ahmad")
    data.seek(5)
    data.read(2)
