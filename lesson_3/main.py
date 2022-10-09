from http.cookies import SimpleCookie


def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    res = {k: v.value for k, v in cookie.items()}
    return res


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('Home=door;') == {'Home': 'door'}
    assert parse_cookie('Home=door=window;size=28;') == {'Home': 'door=window', 'size': '28'}
    assert parse_cookie('name=!!!;') == {'name': '!!!'}
    assert parse_cookie('dog=Mars;') == {'dog': 'Mars'}
    assert parse_cookie('car=bmw;') == {'car': 'bmw'}
    assert parse_cookie('size=45;') == {'size': '45'}
    assert parse_cookie('color=red;') == {'color': 'red'}
    assert parse_cookie('symbol=~~!!') == {'symbol': '~~!!'}
    assert parse_cookie('~~=!!;') == {'~~': '!!'}
    assert parse_cookie('cat=Tom;') == {'cat': 'Tom'}