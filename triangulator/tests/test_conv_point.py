from src.conversion import conversion_point
import pytest

def create_data():
    data_point=[[3,3],[0,1],[5,6]]
    binary=format(len(data_point),"032b")
    for data in data_point:
        binary+=format(data[0],"032b")+format(data[1],"032b")
    return binary,data_point

def test_normal():
    binary,data_point=create_data()
    points=conversion_point(binary)

    assert len(points)==len(data_point)
    for i in range(len(data_point)):
        assert points[i].x==data_point[i][0]
        assert points[i].y==data_point[i][1]

def test_structure():
    binary,_=create_data()

    with pytest.raises(Exception) as exc:
        conversion_point(binary+"1")
    assert exc.value.args[0]=="erreur structure binaire"

def test_type():
    with pytest.raises(Exception) as exc:
        conversion_point("321457805")
    assert exc.value.args[0]=="erreur structure binaire"

def test_nb_point():
    data_point=[[3,3],[0,1],[5,6]]
    binary=format(len(data_point)+1,"032b")
    for data in data_point:
        binary+=format(data[0],"032b")+format(data[1],"032b")
    points=conversion_point(binary+"1")

    assert len(points)==len(data_point)
    for i in range(len(data_point)):
        assert points[i].x==data_point[i][0]
        assert points[i].y==data_point[i][1]

def test_null():
    with pytest.raises(Exception) as exc:
        conversion_point(None) # type: ignore
    assert exc.value.args[0]=="erreur binaire inexistant"

def test_vide():
    with pytest.raises(Exception) as exc:
        conversion_point("")
    assert exc.value.args[0]=="erreur binaire vide"