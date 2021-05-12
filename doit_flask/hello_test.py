def hello(name):
    return 'Hello, {}!'.format(name)


def test_hello():
    assert hello('JOKER') == 'Hello, JOKER!'
