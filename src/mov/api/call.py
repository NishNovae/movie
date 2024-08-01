# call.py
import requests
import os
import pandas as pd
#from datetime import datetime

PARQ_PATH="/home/nishtala/code/movie_saved/"

def echo(yaho):
    return yaho

def apply_type2df(load_dt='20120101', path=PARQ_PATH):
    df = pd.read_parquet(f"{path}/load_dt={load_dt}")
    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 
                'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange',
                'audiInten', 'audiChange']

    for col in num_cols:
        df[col] = pd.to_numeric(df[col])
    return df

def save2df(load_dt='20120101', url_param={}):
    df = list2df(load_dt=load_dt, url_param=url_param)
    df['load_dt'] = load_dt
    df.to_parquet(PARQ_PATH, partition_cols=['load_dt'])
    return df

def list2df(load_dt='20120101', url_param={}):
    l = req2list(load_dt, url_param)
    df = pd.DataFrame(l)
    return df

def req2list(load_dt='20120101', url_param={}) -> list:
    _, data = req(load_dt, url_param=url_param)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    #print(l)

    #df = pd.DataFrame(l)

    return l

def get_key():
    key = os.getenv("MOVIE_API_KEY")
    return key

def req(dt='20120101', url_param={}):
    url = gen_url(dt)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    return code, data

def gen_url(dt="20120101", url_param={}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}" 

    # KEY=VALUE
    for key, value in url_param.items():
        #url += "&multiMovieYn=Y"
        url = url + f"&{key}={value}"

    print("*"*33)
    print(url)
    print("*"*33)

    return url
