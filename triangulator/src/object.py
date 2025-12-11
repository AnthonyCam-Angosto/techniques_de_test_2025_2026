"""Module gerant tout les objets."""

class Point:
    """Objet correspondant a un point."""
    
    x:int
    """Coordonée x du point"""
    y:int
    """Coordonné y du point"""

    def __init__(self,x,y):
        """Initialise de l'objet.
        
        :param x: coordonée x du point
        :param y: coordonée y du point
        """
        self.x=x
        self.y=y
    
    def __str__(self) -> str:
        """Genere la transformation en string."""

        return f"x={self.x}/y={self.y}"

    def __eq__(self, other):
        """Fonction pour vérifier si 2 objet sont les même.
        
        :param other: objet à verifier si c'est le même
        """
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

class Triangle:
    """Objet correspondant à un triangle."""
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
        """Retourne une liste de point."""
        return [self.point1,self.point2,self.point3]
    
    def edges(self):
        p = self.get_points()
        return [(p[0], p[1]), (p[1], p[2]), (p[2], p[0])]
    
    def __eq__(self, other):
        if not isinstance(other, Triangle):
            return False
        return set(self.get_points()) == set(other.get_points())
