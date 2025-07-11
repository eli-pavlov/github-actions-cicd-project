from src.app import app
from bs4 import BeautifulSoup

def test_home_page_loads():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Generate Another Compliment" in response.data  # existing check

def test_generate_button_present():
    client = app.test_client()
    response = client.get('/')
    soup = BeautifulSoup(response.data, 'html.parser')
    button = soup.find('button')
    assert button is not None
    assert 'Generate Another Compliment' in button.text

def test_compliment_changes_on_refresh():
    client = app.test_client()
    compliments = set()
    for _ in range(5):
        response = client.get('/')
        soup = BeautifulSoup(response.data, 'html.parser')
        compliment = soup.find('p')  # changed from h1 to p
        if compliment:
            compliments.add(compliment.text.strip())
    assert len(compliments) >= 2


def test_404_page():
    client = app.test_client()
    response = client.get('/nonexistent')
    assert response.status_code == 404


def test_compliment_is_non_empty():
    client = app.test_client()
    response = client.get('/')
    soup = BeautifulSoup(response.data, 'html.parser')
    compliment = soup.find('p')
    assert compliment and compliment.text.strip() != ""

