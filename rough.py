import random
p = random.randint(1,1000)
d = {1:[2,3],3:[5,5]}
l = d[3]
l[0] = 9
print(d)
