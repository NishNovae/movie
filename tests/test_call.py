# test_call.py
# from src.mov.api.call import gen_url, req, get_key
from src.mov.api.call import *
import pandas as pd

def test_save2df():
    df = save2df('20241231')
    assert isinstance(df, pd.DataFrame)
    assert 'load_dt' in df.columns

def test_hide_key():
    key = get_key()
    assert key

def test_gen_url():
    url = gen_url()

    assert "http" in url
    d = {"multiMovieYn": "N"}
    url = gen_url(req_val = d)
    assert "multiMovieYn" in url

def test_req():
    code, _ = req()
    assert code == 200

    code, _ = req('20230101')
    assert code == 200

def test_req2list():
    l = req2list()
    assert len(l) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'

def test_list2df():
    df = list2df()

    print(df)
    assert isinstance(df, pd.DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'movieNm' in df.columns
    assert 'audiAcc' in df.columns
