from src.conversion import conversion_point,conversion_triangle
from src import triangulation
from src.object import Triangle,Point


def test_conv_to_triangulation():
    data_point=[[0,0],[2,0],[1,2],[3,3],[0,3]]
    binary=format(len(data_point),"032b")
    for data in data_point:
        binary+=format(data[0],"032b")+format(data[1],"032b")
    
    points=conversion_point(binary)
    triangles=triangulation.start(points)

    points_test=list()
    points_test.append(Point(0,0))
    points_test.append(Point(2,0))
    points_test.append(Point(1,2))
    points_test.append(Point(3,3))
    points_test.append(Point(0,3))

    triangles_test=list()
    triangles_test.append(Triangle(points[0],points[1],points[2]))
    triangles_test.append(Triangle(points[0],points[4],points[2]))    
    triangles_test.append(Triangle(points[1],points[2],points[3]))
    triangles_test.append(Triangle(points[2],points[3],points[4]))

    for i in range(len(triangles_test)):
        assert triangles.__contains__(triangles_test[i])


def test_triangulation_to_conv():
    points=[]
    points.append(Point(0,0))
    points.append(Point(2,0))
    points.append(Point(1,2))
    points.append(Point(3,3))
    points.append(Point(0,3))

    triangles=triangulation.start(points)
    binary=conversion_triangle(triangles)
    print("fin")

    triangles_test=[]
    triangles_test.append(Triangle(points[0],points[1],points[2]))
    triangles_test.append(Triangle(points[2],points[1],points[3]))
    triangles_test.append(Triangle(points[0],points[2],points[4]))
    triangles_test.append(Triangle(points[2],points[3],points[4]))  

    point_test=[]
    temp=[0,1,2,3,4]
    binary_test=format(len(temp),"032b")
    for i in temp:
        point_test.append(points[i])
        binary_test+=format(points[i].x,"032b")+format(points[i].y,"032b")

    binary_test+=format(len(triangles_test),"032b")
    for triangle in triangles_test:
        for point in triangle.get_points():
            binary_test+=format(point_test.index(point),"032b")

    assert binary==binary_test

