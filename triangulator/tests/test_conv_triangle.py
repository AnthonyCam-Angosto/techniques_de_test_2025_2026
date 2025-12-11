import pytest
from src.conversion import conversion_triangle
from src.object import Triangle,Point

def create_data():
    triangles=list()
    triangle1=Triangle(Point(1,2),Point(2,3),Point(3,4))
    triangle2=Triangle(Point(4,5),Point(5,6),Point(7,8))
    triangles.append(triangle1)
    triangles.append(triangle2)

    data_point=[[1,2],[2,3],[3,4],[4,5],[5,6],[7,8]]
    binary=format(len(data_point),"032b")
    for data in data_point:
        binary+=format(data[0],"032b")+format(data[1],"032b")

    binary+=format(2,"032b")
    binary+=format(0,"032b")+format(1,"032b")+format(2,"032b")
    binary+=format(3,"032b")+format(4,"032b")+format(5,"032b")
    return triangles,binary


def test_normal():
    triangles,binary_test=create_data()
    binary=conversion_triangle(triangles)
    assert binary==binary_test

def test_null():
    with pytest.raises(Exception) as exc:
        conversion_triangle(None) # type: ignore
    assert exc.value.args[0]=="erreur binaire inexistant"

def test_vide():
    binary=conversion_triangle(list())
    assert binary==(format(0,"032b")+format(0,"032b"))

def test_double():
    points=[]
    points.append(Point(0,0))
    points.append(Point(2,0))
    points.append(Point(1,2))
    points.append(Point(3,3))
    points.append(Point(0,3))

    triangles=[]
    triangles.append(Triangle(points[0],points[1],points[2]))
    triangles.append(Triangle(points[0],points[4],points[2]))
    triangles.append(Triangle(points[1],points[2],points[3]))
    triangles.append(Triangle(points[2],points[3],points[4]))   

    binary=conversion_triangle(triangles)

    point_test=[]
    temp=[0,1,2,4,3]
    binary_test=format(len(temp),"032b")
    for i in temp:
        point_test.append(points[i])
        binary_test+=format(points[i].x,"032b")+format(points[i].y,"032b")

    binary_test+=format(len(triangles),"032b")
    for triangle in triangles:
        for point in triangle.get_points():
            binary_test+=format(point_test.index(point),"032b")

    assert binary==binary_test