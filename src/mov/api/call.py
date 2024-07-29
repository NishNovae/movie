# call.py
import requests
import os
import pandas as pd
#from datetime import datetime

PARQ_PATH="/home/nishtala/code/movie_saved/"


def save2df(load_dt='20120101'):
    df = list2df(load_dt)
    # add load_dt column YYYYMMDD w/ today's date
    df['load_dt'] = load_dt
    # partition based on load_dt
    df.to_parquet(PARQ_PATH, partition_cols=['load_dt'])
    return df

def list2df(load_dt='20120101'):
    l = req2list(load_dt)
    df = pd.DataFrame(l)
    return df

def req2list(load_dt='20120101') -> list:
    _, data = req(load_dt)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    #print(l)

    #df = pd.DataFrame(l)

    return l

def get_key():
    key = os.getenv("MOVIE_API_KEY")
    return key

def req(dt='20120101'):
    url = gen_url(dt)
    r = requests.get(url)
    code = r.status_code
    data = r.json()

    #print(data)
    return code, data

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    return url
