import requests
from bs4 import BeautifulSoup


def define(word: str) -> dict:
    url = f'https://www.wordnik.com/words/{word}'
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    guts = soup.find('div', {'class': 'guts'})

    if guts.p:
        return {'None': guts.p.text}

    source = guts.h3.text
    ul = {
        i: [
            {'abbr': li.abbr.text},
            li.text.split(li.abbr.text)[1].lstrip()] for i, li in enumerate(guts.ul.find_all('li'))
    }

    return {'url': f'https://www.wordnik.com/words/{word}', 'source': source, 'ul': ul}
