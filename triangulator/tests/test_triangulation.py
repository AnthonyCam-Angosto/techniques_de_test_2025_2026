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
    triangles.append(Triangle(points[0],points[1],points[3]))
    triangles.append(Triangle(points[0],points[1],points[4]))
    triangles.append(Triangle(points[0],points[2],points[3]))
    triangles.append(Triangle(points[0],points[2],points[4]))
    triangles.append(Triangle(points[1],points[3],points[4]))
    triangles.append(Triangle(points[1],points[2],points[3]))
    triangles.append(Triangle(points[1],points[2],points[4]))
    triangles.append(Triangle(points[1],points[3],points[4]))
    triangles.append(Triangle(points[2],points[3],points[4]))

    return points,triangles

def test_normal():
    points,triangles_test=create_data()

    triangles=triangulation.start(points)

    assert len(triangles)==len(triangles_test)

    for i in range(len(triangles_test)):
        assert triangles[i].point1==triangles_test[i].point1
        assert triangles[i].point2==triangles_test[i].point2
        assert triangles[i].point3==triangles_test[i].point3

def test_moin3():
    points=list()
    points.append(Point(0,0))
    points.append(Point(2,0))

    triangles=triangulation.start(points)
    assert len(triangles)==0

def test_null():
    triangles=triangulation.start(None)
    assert triangles==None

def test_vide():
    triangles=triangulation.start(list())
    assert triangles==None

def test_erreur_point():
    points,triangles_test=create_data()
    points[0].x=None

    triangles=triangulation.start(points)
    assert triangles==None

def test_colineaire():
    points=list()
    points.append(Point(0,0))
    points.append(Point(1,0))
    points.append(Point(2,0))
    points.append(Point(3,0))
    points.append(Point(4,0))

    triangles=triangulation.start(points)
    assert len(triangles)==0
