import re
from src.object import Point, Triangle

class ConversionError(Exception):
    pass

def conversion_point(binary:str)->list[Point]:
    if(binary==None):
        raise ConversionError("erreur binaire inexistant")
    if(len(binary)%8!=0 or re.match('[01]+',binary)==False):
        raise ConversionError("erreur structure binaire")
    if(binary==""):
        raise ConversionError("erreur binaire vide")

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
    if(triangles==None):
        raise ConversionError("erreur binaire inexistant")
    points=[]
    for t in triangles:
        points.extend(t.get_points())
    
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

    