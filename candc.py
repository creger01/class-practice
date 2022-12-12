class Rectangle:
    """Represents a Rectangle

    attributes: width, length, corner."""

class Point:
    """Represent a point in 2D space."""

box = Rectangle()
box.width = 100.0
box.length = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

# print(type(Rectangle))
# print(type(Point))
# print(type(box.corner))
# <class 'type'>
# <class 'type'>
# <class '__main__.Point'>

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.length/2
    return p

def print_point(p):
    print("(%g, %g)" % (p.x, p.y))

center = find_center(box)
print_point(center)
# (50, 100)

box.width = box.width + 50
box.length = box.length + 100

print(box.width)
print(box.length)
# 150.0
# 300.0

def grow_rectangle(rect, dwidth, dlength):
    rect.width += dwidth
    rect.length += dlength

grow_rectangle(box, 50, 100)

print(box.width)
print(box.length)
# 200.0
# 400.0

p1 = Point()
p1.x =3.0
p1.y = 4.0

import copy
p2 = copy.copy(p1)

print(p1 == p2)
# False

box1 = copy.deepcopy(box)
print(box1 is box) #a copy of something does not make it equal to something else
print(box1.corner is box.corner)
#False
#False
