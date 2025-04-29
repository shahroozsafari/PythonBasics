from datetime import datetime as dt

now_date = dt.now().date()
expire_date = "2025-05-06"
expire_date =  dt.strptime(expire_date,"%Y-%m-%d").date()

if expire_date < now_date :
    print("Expired !")
else :
    print("Useable")

print((now_date - expire_date).days)
