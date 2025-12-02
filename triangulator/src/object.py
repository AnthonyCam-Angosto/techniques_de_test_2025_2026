class Point:
    """
    objet correspondant a un point
    """
    x=None
    y=None

    def __init__(self,x,y):
        """
        
        """
        self.x=x
        self.y=y

class Triangle:
    point1:Point|None=None
    point2:Point|None=None
    point3:Point|None=None

    def __init__(self,point1:Point,point2:Point,point3:Point):
        self.point1=point1
        self.point2=point2
        self.point3=point3