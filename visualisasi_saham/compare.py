import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import requests

dfTlkm = pd.read_csv(
    'saham-TLKM.csv',
    index_col = False,
    parse_dates = ['Tanggal']
)
dfTlkm.set_index('Tanggal', inplace= True)
dfTlkm = dfTlkm.sort_index()
# # print(dfTlkm)

dfIsat = pd.read_csv(
    'saham-ISAT.csv',
    index_col = False,
    parse_dates = ['Tanggal']
)
dfIsat.set_index('Tanggal', inplace= True)
dfIsat = dfIsat.sort_index()
# # print(dfIsat)

dfXL = pd.read_csv(
    'saham-XL.csv',
    index_col = False,
    parse_dates = ['Tanggal']
)
dfXL.set_index('Tanggal', inplace= True)
dfXL = dfXL.sort_index()
# # print(dfXL)

dfFren = pd.read_csv(
    'saham-FREN.csv',
    index_col = False,
    parse_dates = ['Tanggal']
)
dfFren.set_index('Tanggal', inplace= True)
dfFren = dfFren.sort_index()
# # print(dfFren)

##################################################################################################################################################

dfFb = pd.read_csv(
    'FB.csv',
    index_col = False,
    parse_dates = ['Date']
)
dfFb.set_index('Date', inplace= True)
dfFb = dfFb.sort_index()
# print(dfFb)

dfGoog = pd.read_csv(
    'GOOG.csv',
    index_col = False,
    parse_dates = ['Date']
)
dfGoog.set_index('Date', inplace= True)
dfGoog = dfGoog.sort_index()
# print(dfGoog)

dfMsft = pd.read_csv(
    'MSFT.csv',
    index_col = False,
    parse_dates = ['Date']
)
dfMsft.set_index('Date', inplace= True)
dfMsft = dfMsft.sort_index()
# print(dfMsft)

dfApl = pd.read_csv(
    'AAPL.csv',
    index_col = False,
    parse_dates = ['Date']
)
dfApl.set_index('Date', inplace= True)
dfApl = dfApl.sort_index()
# print(dfApl)


url = 'https://kurs.web.id/api/v1/bca'
data = requests.get(url)
matauang = data.json()
# print(matauang)
beli = 1*int(matauang['beli'])
# print(beli)


#####       PLOTTING       #####
plt.style.use('seaborn')
plt.plot(
    dfTlkm.index, dfTlkm['Close']*beli,
    dfIsat.index, dfIsat['Close']*beli,
    dfXL.index, dfXL['Close']*beli,
    dfFren.index, dfFren['Close']*beli,
    dfFb.index, dfFb['Close']*beli/1000000,
    dfGoog.index, dfGoog['Close']*beli/1000000,
    dfMsft.index, dfMsft['Close']*beli/1000000,
    dfApl.index, dfApl['Close']*beli/1000000
)
# set axis #
ax = plt.gca()
ax.xaxis.set_major_locator(md.MonthLocator(
    interval=6
))
ax.xaxis.set_major_formatter(md.DateFormatter(
    '%b %y'
))
plt.xlabel('Bulan')
plt.ylabel('Price')
plt.xticks(rotation=65)
plt.legend(['TLKM','ISAT','XL','FREN','FB','Google','Microsoft','Apple'])
plt.show()

