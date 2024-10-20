import requests


def get_cat_photo():
    url = 'https://api.thecatapi.com/v1/images/search'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data if data else None
        else:
            return None
    except requests.RequestException:
        return None