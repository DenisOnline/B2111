def back_hole(*args):
    print(type(args))
    for i in args:
        print(i)

def back_hole_named(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k, v)

def way(s, t):
    way = s * t
    print(way)

list1 = [90, 18]
dict1 = {"s":90, "t":18}
way(**dict1)