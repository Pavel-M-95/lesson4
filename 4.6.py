from itertools import count
from itertools import cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

num = 0
for el in cycle('ADVDCDVDFDVDDCDV'):
    if num > 20:
        break
    print(el)
    num += 1
