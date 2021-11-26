# import pyupbit
# import WhaleKiller as whale
# import pprint
# import time
#access, secret = whale.KeyValue()
#upbit = pyupbit.Upbit(access, secret)

# tickers = whale.getTickers("KRW")
#
# up_ticker = {}
# ticker_Total = 0
# for ticker in tickers:
#     Total_ask_bid = whale.Total_ask_bid(ticker)
#     if Total_ask_bid > 0:
#         up_ticker[ticker] = Total_ask_bid
#     if ticker_Total <= Total_ask_bid:
#         ticker_name1, ticker_Total = ticker, Total_ask_bid
#     print(ticker, '\t\t', Total_ask_bid)
#     time.sleep(0.08)
#
# print("현재 매수량이 많은 코인 : ", ticker_name1, "매수량= 매수 - 매도 : ", Total_ask_bid)
# print('\n==================================================\n')
# print(up_ticker)
# print(len(up_ticker.keys()))
# print('\n==================================================\n')
# volume_up_ticker = {}
# ticker_volume = 0
# for ticker in up_ticker.keys():
#     volume = whale.get_Volume(ticker, 5).sum() / 10000
#     if ticker_volume <= volume:
#         ticker_name2, ticker_sumVolume = ticker, volume
#     print(ticker, '\t\t', ticker_sumVolume)
#     time.sleep(0.08)
#
# print("현재 거래량이 많은 코인 : ", ticker_name2, "거래량 : ", ticker_sumVolume)
#
# print('\n==================================================\n')
# print(whale.get_Volume("KRW-ALGO", 10), '\t', whale.get_Volume("KRW-ALGO", 10).sum())
# print('\n==================================================\n')
# print(whale.get_Volume("KRW-XEC", 10), '\t', whale.get_Volume("KRW-XEC", 10).sum())
#
# def test_Up_ticker(tickers):
#     up_ticker = {}
#     count = 0
#     for ticker in tickers:
#         Total_ask_bid = whale.ask_bid(ticker)
#         up_ticker[]
#
#         print(count, '/', len(tickers))
#         count += 1
#         time.sleep(0.08)
#
#
#
# def Up_ticker(tickers):
#     up_ticker = {}
#     count = 1
#     for ticker in tickers:
#         Total_ask_bid = ask_bid(ticker)
#         up_ticker[ticker] = Total_ask_bid
#         print(count, '/', len(tickers))
#         count += 1
#         time.sleep(0.08)
#     up_ticker = sorted(up_ticker.items(), key=operator.itemgetter(1), reverse=True)
#     return up_ticker

import pyupbit
import time

tickers1 = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-LTC',
            'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES',
            'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM',
            'KRW-ARDR', 'KRW-ARK', 'KRW-STORJ', 'KRW-GRS', 'KRW-REP',
            'KRW-ADA', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG', 'KRW-ICX',
            'KRW-EOS', 'KRW-TRX', 'KRW-SC', 'KRW-ONT', 'KRW-ZIL',
            'KRW-POLY', 'KRW-ZRX', 'KRW-LOOM', 'KRW-BCH', 'KRW-BAT',
            'KRW-IOST', 'KRW-RFR', 'KRW-CVC', 'KRW-IQ', 'KRW-IOTA',
            'KRW-MFT', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF',
            'KRW-KNC', 'KRW-BSV', 'KRW-THETA', 'KRW-QKC', 'KRW-BTT',
            'KRW-MOC', 'KRW-ENJ', 'KRW-TFUEL', 'KRW-MANA', 'KRW-ANKR',
            'KRW-AERGO', 'KRW-ATOM', 'KRW-TT', 'KRW-CRE', 'KRW-MBL',
            'KRW-WAXP', 'KRW-HBAR', 'KRW-MED', 'KRW-MLK', 'KRW-STPT',
            'KRW-ORBS', 'KRW-VET', 'KRW-CHZ', 'KRW-STMX', 'KRW-DKA',
            'KRW-HIVE', 'KRW-KAVA', 'KRW-AHT', 'KRW-LINK', 'KRW-XTZ',
            'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP',
            'KRW-HUNT', 'KRW-PLA', 'KRW-DOT', 'KRW-SRM', 'KRW-MVL',
            'KRW-STRAX', 'KRW-AQT', 'KRW-GLM', 'KRW-SSX', 'KRW-META',
            'KRW-FCT2', 'KRW-CBK', 'KRW-SAND', 'KRW-HUM', 'KRW-DOGE',
            'KRW-STRK', 'KRW-PUNDIX', 'KRW-FLOW', 'KRW-DAWN', 'KRW-AXS',
            'KRW-STX', 'KRW-XEC', 'KRW-SOL', 'KRW-MATIC', 'KRW-NU',
            'KRW-AAVE', 'KRW-1INCH', 'KRW-ALGO']

all = pyupbit.get_current_price('KRW-ALL')
# for ticker in tickers1:
#     price = pyupbit.get_current_price(ticker)
#     print(ticker, price)
#     time.sleep(0.08)
