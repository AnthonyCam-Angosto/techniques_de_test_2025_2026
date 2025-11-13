from unittest.mock import patch
from src.api import flask
from src import pointSetManager

@patch("triangulation.main")
@patch("conversion.conversion_point")
@patch("pointSetManager.appel")
@patch("conversion.conversion_triangle")
def test_normal_triangulation(mock_triangulation,mock_conv_point,mock_appel,mock_conv_triangle):
    client=flask.test_client()
    mock_triangulation.return_value=[]
    mock_conv_point.return_value=list()
    mock_appel.return_value="011525"
    mock_conv_triangle.return_value="000001001001010100101"

    rep=client.post("/triangulation/123e4567-e89b-12d3-a456-426614174000")
    assert rep.status_code==200

@patch("subprocess.run")
def test_appel_Manager(mock_request):
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = {"PointSet": "0000100010101011010101"}
    id="123e4567-e89b-12d3-a456-426614174000"
    result=pointSetManager.appel(id)
    assert type(result)==type(str)

@patch("subprocess.run")
def test_appel_Manager_erreur_db(mock_request):
    mock_request.return_value.status_code = 503
    mock_request.return_value.json.return_value = {"error": "error"}
    id="123e4567-e89b-12d3-a456-426614174000"
    result=pointSetManager.appel(id)
    assert result==1

@patch("subprocess.run")
def test_appel_Manager_erreur_not_found(mock_request):
    mock_request.return_value.status_code = 404
    mock_request.return_value.json.return_value = {"error": "error"}
    id="123e4567-e89b-12d3-a456-426614174000"
    result=pointSetManager.appel(id)
    assert result==2

@patch("PointSetManager.Appel")
def test_appel_erreur(mock_appel):
    client=flask.test_client()
    mock_appel.return_value=1

    rep=client.post("/triangulation/123e4567-e89b-12d3-a456-426614174000")
    assert rep.status_code==503

@patch("PointSetManager.Appel")
def test_ID_notfound(mock_appel):
    client=flask.test_client()
    mock_appel.return_value=2

    rep=client.post("/triangulation/123e4567-e89b-12d3-a456-426614174000")
    assert rep.status_code==404

def test_id_format():
    client=flask.test_client()

    rep=client.post("/triangulation/123e4567")
    assert rep.status_code==400
