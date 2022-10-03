from urllib import parse as p


def parse(query: str) -> dict:
    p.urlsplit(query)
    p.parse_qs(p.urlsplit(query).query)
    result = dict(p.parse_qsl(p.urlsplit(query).query))
    return result 


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?car=bmw&color=red') == {'car': 'bmw', 'color': 'red'}
    assert parse('https://example.com/path/to/page?size=12&color=purple') ==  {'size': '12', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?file=home&size=12') == {'file': 'home', 'size': '12'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple')
    assert parse('https://example.com/path/to/page?name=!&12=!!') == {'name': '!', '12': '!!'}
    assert parse('https://example.com/path/to/page?**=12&!!=~~') == {'**': '12', '!!': '~~'}
    assert parse('https://example.com/path/to/page?q=w&e=r') == {'q': 'w', 'e': 'r'}
    assert parse('https://example.com/path/to/page?дом=дверь&стол=тарелка') == {'дом': 'дверь', 'стол': 'тарелка'}
    assert parse('https://example.com/path/to/page?Тима=Тома&Тима=Тома') == {'Тима': 'Тома', 'Тима': 'Тома'}
    assert parse('https://example.com/path/to/page?=&') == {}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
