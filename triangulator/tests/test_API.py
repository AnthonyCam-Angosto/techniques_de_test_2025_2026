from unittest.mock import patch
from urllib.error import HTTPError
from src.api import app
from src import pointSetManager

@patch("src.triangulation.start")
@patch("src.conversion.conversion_point")
@patch("src.pointSetManager.appel")
@patch("src.conversion.conversion_triangle")
def test_normal_triangulation(mock_conv_triangle,mock_appel,mock_conv_point,mock_triangulation):
    app.testing = True
    client=app.test_client()
    mock_triangulation.return_value=[]
    mock_conv_point.return_value=[]
    mock_appel.return_value="011525"
    mock_conv_triangle.return_value="000001001001010100101"

    rep=client.get("/triangulation/123e4567-e89b-12d3-a456-426614174000")
    assert rep.status_code==200
    assert rep.data==b'000001001001010100101'

@patch("src.pointSetManager.appel")
def test_appel_erreur(mock_appel):
    app.testing = True
    client=app.test_client()
    mock_appel.return_value=1

    rep=client.get("/triangulation/123e4567-e89b-12d3-a456-426614174000")
    assert rep.status_code==503

@patch("src.pointSetManager.appel")
def test_id_notfound(mock_appel):
    app.testing = True
    client=app.test_client()
    mock_appel.return_value=2

    rep=client.get("/triangulation/123e4567-e89b-12d3-a456-426614174000")
    assert rep.status_code==404

def test_id_format():
    app.testing = True
    client=app.test_client()

    rep=client.get("/triangulation/123e4567")
    assert rep.status_code==400



class _DummyHeaders:
    def get_content_charset(self):
        return "utf-8"
    
class _DummyResponse:
    def __init__(self, data: bytes):
        self._data = data
        self.headers = _DummyHeaders()

    def read(self):
        return self._data


def test_appel_manager(monkeypatch):
    dummy=_DummyResponse(b"0000100010101011010101")
    monkeypatch.setattr(pointSetManager.request, "urlopen", lambda url: dummy)
    id_ps="123e4567-e89b-12d3-a456-426614174000"
    result=pointSetManager.appel(id_ps)
    assert isinstance(result,str)


def test_appel_manager_erreur_db(monkeypatch):
    def raiser(url):    
        raise HTTPError("http://",503,"The PointSet storage layer (database) is unavailable.",None,None)# type: ignore 
    monkeypatch.setattr(pointSetManager.request,"urlopen",raiser)
    id_ps="123e4567-e89b-12d3-a456-426614174000"
    result=pointSetManager.appel(id_ps)
    assert result==1

def test_appel_manager_erreur_not_found(monkeypatch):
    def raiser(url):    
        raise HTTPError("http://",404,"A PointSet with the specified ID was not found.",None,None)# type: ignore 
    monkeypatch.setattr(pointSetManager.request,"urlopen",raiser)
    id_ps="123e4567-e89b-12d3-a456-426614174000"
    result=pointSetManager.appel(id_ps)
    assert result==2
