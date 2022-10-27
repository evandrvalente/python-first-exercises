import random
from collections import Counter

number_list = []

for x in range(10000):
    number_list.append(random.randint(0,1000))

#print(number_list)

counter1 = Counter(number_list)
print(counter1)
print(counter1[13])

most_commons = counter1.most_common()
print(most_commons)