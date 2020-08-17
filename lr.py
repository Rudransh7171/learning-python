import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig = plt.figure()
data = pd.read_csv("C:/Users/rudra/Downloads/data.csv.csv")#file location of data sets
y = data['Father'].values
x = data['Son'].values
c = 0
d = 0
for i in x:
    
    c += int(i)
means = c/len(x)
for i in y:
    d += int(i)
meanf = d/len(y)
e = []
f = []
l  = 0
for i in x:
    e.append(i-means)
for i in y:
    f.append(i-meanf)
for i in f:
    l+=i
prod  = []
for j,k in zip(e,f):
    prod.append(j*k)
j = []
for i in e:
    j.append(i**2)
sum1 = 0
sum2 = 0
for i in prod:
    sum1 += i
for i in j:
    sum2 += i
div = sum1/sum2
#div = slope
c = meanf - div*means
#now predticting the age of son
ypred = []
for i in x:
    ypred.append(div*i+c)
z = []
q = []
for i in ypred:
    z.append(i-meanf)
for i in z:
    q.append(i**2)
o = 0
for i in q:
    o +=i
v = []
for i in f:
    v.append(i**2)
t = 0
for i in v:
    t += i
div2 = o/t
plt.xlabel('Son')
plt.ylabel('father')
plt.scatter(x,y)
plt.scatter(x,ypred)
plt.show()
print(div2)#R(sq) vaue
