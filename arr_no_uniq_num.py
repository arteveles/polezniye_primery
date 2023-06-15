import pandas as pd
from collections import Counter


i = [1, 2, 4, 5]
j = [3, 3, 4]
k = [2, 3, 4, 5, 6]
lst = []

for x in i:
    if x in j and k:
        lst.append(x)
print(lst)


