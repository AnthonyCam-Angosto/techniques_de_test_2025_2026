import re
from src.object import Point, Triangle

class ConversionError(Exception):
    pass

def conversion_point(binary:str)->list[Point]:
    if(len(binary)%8!=0 or re.match('[01]+',binary)==False):
        raise ConversionError("erreur structure binaire")

    pointset=[]
    size_byte=4*8
    nb=int(binary[:size_byte],2)
    if((len(binary[size_byte:])/(8*8))!=nb):
        nb=int(len(binary[size_byte:])/8)

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



def conversion_triangle(triangles)->str:
    pass