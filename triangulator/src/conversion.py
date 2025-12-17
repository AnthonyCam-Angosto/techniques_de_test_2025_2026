"""Ce module gere la conversion d'objet en binaire et l'inverse."""
import re

from src.object import Point, Triangle


class ConversionError(Exception):
    """Exception s'il y a des erreur durant la conversion."""
    
    pass

def conversion_point(binary:str)->list[Point]:
    """Conversion d'un PointSet en binaire en liste d'objet Point.

    Params:
        binary(str):PointSet en binaire
    
    Returns:
        list[Point]: liste des point du PointSet

    """
    if(binary is None):
        raise ConversionError("erreur binaire inexistant")
    if(len(binary)%8!=0 or not re.match('[01]+',binary)):
        raise ConversionError("erreur structure binaire")

    pointset=[]
    size_byte=4*8
    nb=int(binary[:size_byte],2)
    if((len(binary[size_byte:])/(8*8))!=nb):
        nb=int(len(binary[size_byte:])/(8*8))

    start=size_byte
    end=start+size_byte
    for _ in range(nb):
        x=int(binary[start:end],2)
        start+=size_byte
        end+=size_byte
        y=int(binary[start:end],2)
        pointset.append(Point(x,y))
        start+=size_byte
        end+=size_byte
    return pointset



def conversion_triangle(triangles:list[Triangle])->str:
    """Conversion d'une liste de triangles en binaire.
    
    Params:
        triangles(list[Triangle]):list de triangle 
    
    Returns:
        str: liste de triangle en binaire

    """
    if(triangles is None):
        raise ConversionError("erreur binaire inexistant")
    points=[]
    for t in triangles:
        for point in t.get_points():
            if(not points.__contains__(point)):
                points.append(point)
    
    bin_vert=format(len(points),"032b")
    for point in points:
        bin_vert+=format(point.x,"032b")+format(point.y,"032b")
    
    bin_triangle=format(len(triangles),"032b")
    for t in triangles:
        for point in t.get_points():
            i=points.index(point)
            bin_triangle+=format(i,"032b")

    result=bin_vert+bin_triangle
    return result

    