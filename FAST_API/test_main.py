from starlette.testclient import TestClient

from main import app

client = TestClient(app)


# create_location TESTS
def test1_read_main():
    response = client.post("/post_location?pin=63212453&latitude=123&longitude=123&place_name=123&admin_name1=123")
    assert response.status_code == 200

# get_location TESTS
def test3_read_main():
    response = client.get("/get_location?lat__=234&lng__=234")
    assert response.status_code == 200
    assert response.json() == {"admin_name1": "23456789", "latitude": 234,"longitude": 234, "key": "IN/100001 ", "place_name": "sdfg"}

def test4_read_main():
    response = client.get("/get_location?lat__=1234&lng__=1234")
    assert response.status_code == 200


# get_points_using_postgres
def test5_read_main():
    response = client.get("/get_using_postgre?lat_=27.0333&lng_=88.3667")
    assert response.status_code == 200

#get_points_using_postgres
def test6_read_main():
    response = client.get("/get_using_self?lat_=28.55&lng_=77.2667")
    assert response.status_code == 200


#get_ detect_city_with_lat&lng
def test7_read_main():
    response = client.get("/detect?lat__=28.55&lng__=77.2667")
    assert response.status_code == 200


