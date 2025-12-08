from operator import truediv


class Point:
    """
    objet correspondant a un point
    """
    x:int
    y:int

    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self) -> str:
        return f"x={self.x}/y={self.y}"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

class Triangle:
    point1:Point
    point2:Point
    point3:Point

    def __init__(self,point1:Point,point2:Point,point3:Point):
        self.point1=point1
        self.point2=point2
        self.point3=point3
    
    def __iter__(self):
        return iter([self.point1, self.point2, self.point3])
    
    def get_points(self):
        return [self.point1,self.point2,self.point3]
    
    def edges(self):
        p = self.get_points()
        return [(p[0], p[1]), (p[1], p[2]), (p[2], p[0])]
    
    def __eq__(self, other):
        if not isinstance(other, Triangle):
            return False
        return set(self.get_points()) == set(other.get_points())
