import csv
import math

with open ("data.csv") as f:
    reader=csv.reader(f)
    new_data=list(reader)

data=new_data[0]

def mean(data):
    length=len(data)
    sum=0
    for i in data:
        sum=sum+int(i)

    mean=sum/length
    return mean

sq_list=[]
for i in data:
    a=int(i)-mean(data)
    a=a ** 2
    sq_list.append(a)

total=0
for i in sq_list:
    total=total+i

result=total/(len(data)-1)
std_dev=math.sqrt(result)
print(std_dev)
