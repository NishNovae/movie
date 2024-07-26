# test_call.py
# from src.mov.api.call import gen_url, req, get_key
from src.mov.api.call import *

def test_hide_key():
    key = get_key()
    assert key

def test_gen_url():
    url = gen_url()

    assert "http" in url
    assert "kobis" in url

def test_req():
    code, data = req()
    assert code == 200

    code, data = req('20230101')
    assert code == 200

def test_req2():
    l = req2dataframe()
    assert l is not None
