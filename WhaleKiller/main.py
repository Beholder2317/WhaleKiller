import WhaleKiller as whale
import pyupbit
import pprint
import time


#access, secret = whale.KeyValue()
#upbit = pyupbit.Upbit(access, secret)

# tickers = whale.getTickers("KRW")
# print(tickers)
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


print('\n==================================================\n'
      '\t\t\t ticker search start!!! \t\t\t'
      '\n==================================================\n')

print('\t\t\t search Up_ticker!!! \t\t\t')
Up_ticker = whale.Up_ticker(tickers1)
# pprint.pprint(Up_ticker)
print(len(Up_ticker))
print(type(Up_ticker))
pprint.pprint(Up_ticker)
print('\n==================================================\n')

print('\t\t\t search Volume_ticker!!! \t\t\t')
Volume_ticker = whale.Volume_ticker(tickers1)
# pprint.pprint(Volume_ticker)
print(len(Volume_ticker))
print(type(Volume_ticker))
pprint.pprint(Volume_ticker)
print('\n==================================================\n')

# up_ticker = {}
# for ticker in tickers:
#     Total_ask_bid = whale.Total_ask_bid(ticker)
#     if Total_ask_bid > 0:
#         up_ticker[ticker] = Total_ask_bid
#     time.sleep(0.08)
#
# up_ticker = sorted(up_ticker.items(), key=operator.itemgetter(1), reverse=True)
#
# pprint.pprint(up_ticker)
# print(len(up_ticker))