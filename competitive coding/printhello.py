import math
import random
initial = 1000
final=initial
n=1000
for i in range(n):
    final*=random.choice([1.5,0.5])
print(initial,final)
print(math.sqrt(0.5*1.5))
print((final/initial)**(1/n))
