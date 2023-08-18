from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)

#print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")

n = int(input("enter some number: "))
ans={i : i*i for i in range(1,n+1)}
print(ans)