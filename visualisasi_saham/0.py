import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv(
    'data-histori-saham.csv',
    index_col=False,
    parse_dates=['Tanggal'])        ## NOTES!!! ini penting saat kita membuat tgl jadi index
df.set_index('Tanggal', inplace=True)
df = df.sort_index()       ## kalau gakmau pakai inplace
# print(df)
# print(df['2016-01':'2017-01'])
# print(df.loc['2017-10-02']['Close'])    ## only print Close's column, formatnya harus tahun-bulan-tanggal
# print(df.loc['2019-03']['Close'].mean())        ## cari rata2 di bulan Maret
# print(df[df['Close']==df['Close'].max()])       ## search data max di kolom close
# print(df['2019-02-01':'2019-05-01'].count())    ## untuk print jumlah values nya

# plt.plot(
#     df.index, df['Close'], 'r-'
# )
# plt.style.use('seaborn')    ## declair ini sebelum plt.plot kalau mau pake style seaborn
# plt.plot(
#     df['2019-02-01':'2019-05-01'].index, df['2019-02-01':'2019-05-01']['Close'], 'r-'     ## hanya tahun 2019
# )
# plt.subplots_adjust(bottom=.21)
# plt.xlabel('Tanggal')
# plt.ylabel('Rupiah')
# plt.xticks(rotation=60)
# plt.grid(True)
# ##### biar tanggal rapih, perhatikan yg bawah. Inget!!!! Catet diotak!!!! Harus Bisa LULUS ujian modul 2!!!!!!!
# ax = plt.gca()  # get current axis
# ax.xaxis.set_major_locator(mdates.DayLocator(   ## atur posisi biar rapih, kalau mau perbulan tinggal ganti Day jadi Month, kalau perminggu tinggal ganti Weekday
#     interval=5       ## menunjukkan 5 hari, jadi interval itu ya intervalnya, ya gitu dah pokoknya
# ))
# ax.xaxis.set_major_formatter(mdates.DateFormatter(   ## atur format biar rapih, kalau Y besar angkanya lengkap, kalau y kecil berarti hanya 2 angka terakhir yang ditampilkan
#     '%d-%m-%Y'
# ))
# plt.show()


#########   tampilkan semua data
# plt.style.use('seaborn') 
# plt.plot(
#     df.index, df['Close'], 'r-'     
# )
# plt.subplots_adjust(bottom=.21)
# plt.xlabel('Tanggal')
# plt.ylabel('Rupiah')
# plt.xticks(rotation=60)
# plt.grid(True)
# ax = plt.gca()
# ax.xaxis.set_major_locator(mdates.YearLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter(
#     '%Y'
# ))
# plt.show()

#######     RESAMPLE
# M => MonthEnd, W => WeekEnd, Q => Quarter, Y => Yearly
# print(df.resample('M').mean())  ## rata-rata bsetiap kolom di akhir bulan. Simbol M itu Month, makanya hasil yang ditampilin adalah data setiap akhir bulan
# print(df['2019-02':'2019-05']['Close'].resample('M').mean())


