import random as r
import matplotlib.pyplot as plt

random_x = []
random_y = []
function_x = []
function_y = []
point = 0

xmin = 0
xmax = 25
ymin = 0
ymax = 600


for i in range(xmax+1):
    j = i ** 2 - 3 * i + 4
    function_x.append(i)
    function_y.append(j)

for i in range(4000):
    random_x.append(r.randint(xmin, xmax))
    random_y.append(r.randint(ymin, ymax))

plt.plot(random_x, random_y)
plt.plot(function_x, function_y)

for i in range(4000):
    for x in range(xmax+1):
        y = x ** 2 - 3 * x + 4
        if random_x[i] == x and random_y[i] < y:
            point += 1

print(point)

"""Label"""
plt.title("Random")
plt.show()