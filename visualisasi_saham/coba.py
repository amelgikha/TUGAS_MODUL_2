import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import requests


#######     CARA ISI KOLOM YANG HILANG BIAR VISUALISASI BAGUS   ##############
# df = df.resample('D').sum() ## hasilnya udah pasti 0.0
# print (df)
# tinggal di replace => df = df.replace(0, np.NaN) setelah itu tinggal diganti value-nya. Pastikan jangan di drop!
# df = df.fillna(method='bfill'atau bisa juga 'ffill', axis='index') TAPI kebanyakan dipake samain sama data yang terakhir
# berarti kalau mau plotting, perhatikan dan pastikan dulu apakah ada data yang masih kosong.
# tambah kolom => df['x']np.arrange(362). 362 ini dapet dari hasil count() karena datanya ada 362 baris jadi tinggal diisi


df = pd.read_csv(
    'AAPL.csv',
    index_col = False,
    parse_dates = ['Date']
)

dfcoba = df[['Open','Close']]
# print(df)

dfcoba.columns = ['Est','Tes']  ## ganti nama kolom
print(dfcoba)

# dfApl['s']= dfApl[dfApl['Close'] - dfApl['Open']]
# df['selisih']= df.apply(
#     lambda baris : baris['Open'] - baris['Close'],
#     axis=1)


# df['sex']= df.apply(
#     lambda sex : sex['Est'] - sex['Tes'],
#     axis=1
# )


# df['sex'] = df.apply(
#     lambda x: 'WANITA' if x ['Est'] > x['Tes'] else(
#         '---' if x ['Open'] == x['Close'] else 'PRIA'
#     ),
#     axis=1
# )
# print(df)