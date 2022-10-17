

d = {}
d["a"] = 2
print(d)
print("a" in d)

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
a = ",".join(list(sorted_x))
print(a)