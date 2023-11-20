#requests to api

import requests

def test_home_request():
	response = requests.get("http://127.0.0.1:8000")
	assert response.status_code == 200
	assert response.text == '{"Hello":"World!!!"}'