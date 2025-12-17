import time,logging
from src.object import Triangle,Point
from src import triangulation
from src.conversion import conversion_point, conversion_triangle
import pytest
import random

logger=logging.getLogger(__name__)
logging.basicConfig(filename='performance.log', level=logging.INFO)


def create_data(hard=False):
    points=list()
    points.append(Point(0, 0))
    points.append(Point(1, 2))
    points.append(Point(2, 4))
    points.append(Point(3, 1))
    points.append(Point(4, 3))
    points.append(Point(5, 5))
    points.append(Point(6, 2))
    points.append(Point(7, 4))
    points.append(Point(8, 1))
    points.append(Point(9, 3))
    points.append(Point(10, 5))
    points.append(Point(11, 2))
    points.append(Point(12, 4))
    points.append(Point(13, 0))
    points.append(Point(14, 3))
    if(hard):
        points.append(Point(15, 1))
        points.append(Point(16, 4))
        points.append(Point(17, 2))
        points.append(Point(18, 5))
        points.append(Point(19, 3))
        points.append(Point(20, 0))
        points.append(Point(21, 2))
        points.append(Point(22, 4))
        points.append(Point(23, 1))
        points.append(Point(24, 3))
    return points

@pytest.mark.perf
def test_perf_triangulation_low():
    points=list()
    points.append(Point(0,0))
    points.append(Point(2,0))
    points.append(Point(1,2))

    time1=time.time()
    triangles=triangulation.start(points)
    time2=time.time()
    result=time2-time1

    logger.info("test performance : triangulation 1 triangle =",result,'s')
    assert result<0.05

@pytest.mark.perf
def test_perf_triangulation_medium():
    #15 point/21 triangles
    points=create_data()

    time1=time.time()
    triangles=triangulation.start(points)
    time2=time.time()
    result=time2-time1

    logger.info("test performance : triangulation 12 point =",result,'s')
    assert result<0.1

@pytest.mark.perf
def test_perf_triangulation_hard():
    #25 point/ 41 triangles
    points=create_data(hard=True)

    time1=time.time()
    triangles=triangulation.start(points)
    time2=time.time()
    result=time2-time1

    logger.info("test performance : triangulation 20 point =",result,'s')
    assert result<0.5

@pytest.mark.perf
def test_perf_convTriangles_low():
    # 1 triangle
    points=[]
    points.append(Point(0,0))
    points.append(Point(2,0))
    points.append(Point(1,2))
    triangles=[]
    triangles.append(Triangle(points[0],points[1],points[2]))

    time1=time.time()
    val=conversion_triangle(triangles)
    time2=time.time()
    result=time2-time1

    logger.info("test performance : conv_Triangle 1 triangle =",result,'s')
    assert result<0.005

@pytest.mark.perf
def test_perf_convTriangles_medium():
    #15 triangles
    points=create_data()
    triangles=list()
    r=random.Random()
    for _ in range(30):
        triangles.append(Triangle(points[r.randint(0,14)],points[r.randint(0,14)],points[r.randint(0,14)]))

    time1=time.time()
    val=conversion_triangle(triangles)
    time2=time.time()
    result=time2-time1

    logger.info("test performance : conv_Triangle 15 triangle =",result,'s')
    assert result<0.01

@pytest.mark.perf
def test_perf_convTriangles_hard():
    #30 triangles
    points=create_data(hard=True)
    triangles=list()
    r=random.Random()
    for _ in range(30):
        triangles.append(Triangle(points[r.randint(0,24)],points[r.randint(0,24)],points[r.randint(0,24)]))

    time1=time.time()
    val=conversion_triangle(triangles)
    time2=time.time()
    result=time2-time1

    logger.info("test performance : conv_Triangle 30 triangle =",result,'s')
    assert result<0.03

@pytest.mark.perf
def test_perf_convPoint_low():
    # 3 points
    nb_point=3

    binary=format(nb_point,"032b")
    for i in range(nb_point):
        binary+=format(i,"032b")+format(i,"032b")

    time1=time.time()
    val=conversion_point(binary)
    time2=time.time()
    result=time2-time1

    logger.info("test performance : conv_Point 3 points =",result,'s')
    assert result<0.005

@pytest.mark.perf
def test_perf_convPoint_medium():
    # 15 points
    nb_point=15

    binary=format(nb_point,"032b")
    for i in range(nb_point):
        binary+=format(i,"032b")+format(i,"032b")

    time1=time.time()
    val=conversion_point(binary)
    time2=time.time()
    result=time2-time1

    logger.info("test performance : conv_Point 15 points =",result,'s')
    assert result<0.01

@pytest.mark.perf
def test_perf_convPoint_hard():
    # 40 points
    nb_point=40

    binary=format(nb_point,"032b")
    for i in range(nb_point):
        binary+=format(i,"032b")+format(i,"032b")

    time1=time.time()
    val=conversion_point(binary)
    time2=time.time()
    result=time2-time1

    logger.info("test performance : conv_Point 40 points =",result,'s')
    assert result<0.03