class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print('origin')
        case Point(x=0, y=y):
            print(f'y={y}')
        case Point(x=x, y=0):
            print(f'x={x}')
        case Point():
            print('somewhere else')
        case _:
            print('not a point')

point = Point()
point.x = 0
point.y = 2
where_is(point)