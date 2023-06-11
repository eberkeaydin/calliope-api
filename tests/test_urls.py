import requests

def test_quiz_url():
    response = requests.get("http://localhost:8080/quiz")
    assert response.status_code == 200

def test_admin_url():
    response = requests.get("http://localhost:8080/admin")
    assert response.status_code == 200
