#!/usr/bin/env python
#coding:utf-8

"""
Cuboid layers

The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.

If we then add a second layer to this solid it would require forty-six cubes to cover every visible face, the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen cubes to cover every visible face.
However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.
We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.
It turns out that 154 is the least value of n for which C(n) = 10.
Find the least value of n for which C(n) = 1000.

"""
from collections import defaultdict

def calculate_layer(x,y,z,L):   
    return 2*(2*(L-1)*(x+z)+2*(L-1)*(L+y-2)+x*y+x*z+y*z)

dict1 = defaultdict(int)
max_v = 20000

for L in range(1,100):
    for x in range(1,5000):
        if calculate_layer(x,x,x,L) > max_v:
            break
        for y in range(x,5000):
            if calculate_layer(x,y,y,L) > max_v:
                break
            for z in range(y,5000):
                if calculate_layer(x,y,z,L) > max_v:
                    break
                dict1[calculate_layer(x,y,z,L)] += 1

for x,y in dict1.iteritems():
    if y == 1000:
        print x

# 18522