import requests
from bs4 import BeautifulSoup

def get_coordinates(location: str) -> list:
    url: str = f"https://pl.wikipedia.org/wiki/{location}"

    headers = {
        'User-Agent': 'MyBot/1.0 (ja@example.com)'
    }

    response = requests.get(url, headers=headers)

    response_html = BeautifulSoup(response.text, "html.parser")

    response_html_lat = float(response_html.select(".latitude")[1].text.replace(',', '.'))
    response_html_lng = float(response_html.select(".longitude")[1].text.replace(',', '.'))

    return [response_html_lat, response_html_lng]


if __name__ == "__main__":
    print(get_coordinates("Warszawa"))