class Point:
    """Represents a point in 2-D space."""

print(type(Point))
#<class 'type'>

myPoint = Point()
print(type(myPoint))
# <class '__main__.Point'>

myPoint.x = 0
myPoint.y = 2

print(myPoint.x)
print(myPoint.y)
# 0
# 2

print("(%d, %d)"% (myPoint.x, myPoint.y))
# (0, 2)

myPoint.x =3
myPoint.y = 4

import math

def distance_from_origin(p):
    distance = math.sqrt(p.x**2 + p.y**2)
    print(distance)

distance_from_origin(myPoint)
# 5.0
