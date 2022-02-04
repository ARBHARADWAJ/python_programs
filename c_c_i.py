import collections
from dis import dis
from typing import Counter


from collections import Counter
dist={}
list=[1,2,1,2,1,3]
dist=Counter(list)
print(dist)
for num in dist:
    if dist[num]==1:
        print(num)
#    print(dist[num])
