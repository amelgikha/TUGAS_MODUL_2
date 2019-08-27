import pandas as pd
import pymongo

x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['blabla']
col = db['mongobla']
data = list(col.find())

df = pd.DataFrame(data)
print(df)