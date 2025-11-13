from src.conversion import conversion_point

def create_data():
    data_point=[[3,3],[0,1],[5,6]]
    binary=format(len(data_point),"032b")
    for data in data_point:
        binary+=format(data[0],"032b")+format(data[1],"032b")
    return binary,data_point

def test_normal():
    binary,data_point=create_data()
    Points=conversion_point(binary)

    assert len(Points)==len(data_point)
    for i in range(len(data_point)):
        assert Points[i].x==data_point[i][0]
        assert Points[i].y==data_point[i][1]

def test_structure():
    binary,data_point=create_data()
    Points=conversion_point(binary+"1")
    assert Points==None

def test_type():
    Points=conversion_point("321457805")
    assert Points==None

def test_nb_point():
    data_point=[[3,3],[0,1],[5,6]]
    binary=format(len(data_point)+1,"032b")
    for data in data_point:
        binary+=format(data[0],"032b")+format(data[1],"032b")
    Points=conversion_point(binary+"1")

    assert len(Points)==len(data_point)
    for i in range(len(data_point)):
        assert Points[i].x==data_point[i][0]
        assert Points[i].y==data_point[i][1]

def test_null():
    Points=conversion_point(None)
    assert Points==None

def test_vide():
    Points=conversion_point("")
    assert Points==None