import pytest
from src import triangulation
from src.object import Point, Triangle

def create_data():
    points=list()
    points.append(Point(0,0))
    points.append(Point(2,0))
    points.append(Point(1,2))
    points.append(Point(3,3))
    points.append(Point(0,3))

    triangles=list()
    triangles.append(Triangle(points[0],points[1],points[2]))
    triangles.append(Triangle(points[0],points[4],points[2]))    
    triangles.append(Triangle(points[1],points[2],points[3]))
    triangles.append(Triangle(points[2],points[3],points[4]))

    return points,triangles

def test_normal():
    points,triangles_test=create_data()

    triangles=triangulation.start(points)
    assert len(triangles)==len(triangles_test)

    for i in range(len(triangles_test)):
        assert triangles.__contains__(triangles_test[i])

def test_moin3():
    points=list()
    points.append(Point(0,0))
    points.append(Point(2,0))

    triangles=triangulation.start(points)
    assert len(triangles)==0

def test_null():
    with pytest.raises(Exception) as exc:
        triangulation.start(None)
    assert exc.value.args[0]=="erreur pointset inexistant"

def test_vide():
    with pytest.raises(Exception) as exc:
        triangulation.start([])
    assert exc.value.args[0]=="erreur pointset vide"

def test_erreur_point():
    points,_=create_data()
    points[0].x=None

    with pytest.raises(Exception) as exc:
        triangulation.start(points)
    assert exc.value.args[0]=="erreur durant la triangulation"

def test_colineaire():
    points=list()
    points.append(Point(0,0))
    points.append(Point(1,0))
    points.append(Point(2,0))
    points.append(Point(3,0))
    points.append(Point(4,0))

    triangles=triangulation.start(points)
    assert len(triangles)==0
