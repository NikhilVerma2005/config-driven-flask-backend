def test_login_success(client):
    response = client.post(
        "/login",
        json = {"username":"nik", "password":"pass123"}
    )
    assert response.status_code == 200


