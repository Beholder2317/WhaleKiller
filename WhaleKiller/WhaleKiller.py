import numpy
import pyupbit
import json
import datetime
import pprint
import pandas
import time
import operator

# 업비트 API 키값
def KeyValue():
    str = './KeyValue.json'#input("API Key값 위치(.json) : ")==
    with open(str,'r') as f:
        json_data = json.load(f)
    access, secret = json_data['access'], json_data['secret']
    return access, secret

# 해당 티커 목록 조회
def getTickers(str):
    tickers = pyupbit.get_tickers(str.upper())
    print(len(tickers),'\t',type(tickers))
    return tickers


# 현재 시간 문자열 반환 함수
def SetNowTime():
    now = datetime.datetime.now()
    # dateNow = datetime.datetime.now() + datetime.timedelta(minutes=-1)
    dateNow_string = now.strftime('%Y%m%d%H%M%S')

    return dateNow_string

# 거래량을 조회하는 코드
'''
pyupbit.get_ohlcv(ticker, interval, count)
ticker: 조회를 원하는 심볼값
interval: 조회를 하고자 하는 차트 종류 (ex: 1분, 30분, 일 ...)
count: 조회하고자 하는 데이터의 수 (캔들 개수)
pandas 데이터로 반환
pandas 데이터 
거래량 합은 sum()함수로 구할 수 있음
# '''
def get_Volume(ticker, cnt):
    volume = pyupbit.get_ohlcv(ticker=ticker,
                               count= int(cnt),
                               interval="minute1",
                               to=datetime.datetime.now() + datetime.timedelta(minutes=-1),
                               period=1)['volume']
    return volume

# 호가 계산
'''
get_orderbook() 딕셔너리 반환
market :
orderbook_units : [ ask_price :
                    ask_size :
                    bid_price :
                    bid_size : ]    x 15
timestamp : 
total_ask_size :
total_bid_size :
'''
def ask_bid(ticker):
    orderbook = pyupbit.get_orderbook(ticker)
    Total_ask = orderbook['total_ask_size']
    Total_bid = orderbook['total_bid_size']
    return Total_bid - Total_ask

def Up_ticker(tickers):
    up_ticker = []
    count = 1
    for ticker in tickers:
        Total_ask_bid = ask_bid(ticker)
        up_ticker.append(Total_ask_bid)
        print(count, '/', len(tickers))
        count += 1
        time.sleep(0.08)
    return dict(up_ticker)

def Volume_ticker(tickers):
    volume_ticker = {}
    count = 1
    for ticker in tickers:
        volume = get_Volume(ticker, 5).sum()
        volume_ticker[ticker] = volume
        print(count, '/', len(tickers))
        count += 1
        time.sleep(0.08)
    return dict(volume_ticker)

def mkdic(tickers, list):
    mkdic = dict(zip(tickers, list))
    return mkdic



#
# up_ticker = sorted(up_ticker.items(), key=operator.itemgetter(1), reverse=True)