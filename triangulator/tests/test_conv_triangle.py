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
        conversion_triangle(None)
    assert exc.value.args[0]=="erreur binaire inexistant"

def test_vide():
    binary=conversion_triangle(list())
    assert binary==(format(0,"032b")+format(0,"032b"))

