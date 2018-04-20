import pants
import math
import random

nodes = []

for i in range(0,100):
 nodes.append((random.uniform(0,100), random.uniform(0,100)))

print(nodes)


def fn(a, b):
    return math.sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))

monde = pants.World(nodes, fn)

solver = pants.Solver()
sol = solver.solve(monde)




