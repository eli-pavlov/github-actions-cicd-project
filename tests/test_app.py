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
        compliment = soup.find('h1')  # assuming compliment is inside <h1>
        if compliment:
            compliments.add(compliment.text.strip())
    # Expect at least 2 different compliments
    assert len(compliments) >= 2
