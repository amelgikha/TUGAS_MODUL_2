import plotly.graph_objects as go
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'taikucing',
    database = 'world'
)

query1 = '''select country.Name as Negara_ASEAN, country.Population as Populasi_Negara, GNP, city.Name as IbuKota, city.Population as Populasi_Ibukota from
country inner join city
on country.Capital = city.ID where country.Name = 'Brunei' or country.Name ='Cambodia' or country.Name ='East Timor' or country.Name ='Indonesia' or country.Name ='Laos' or country.Name ='Malaysia' or country.Name ='Myanmar' or country.Name ='Philippines'or country.Name ='Singapore' or country.Name ='Thailand' or country.Name ='Vietnam' order by country.Name asc'''

df = pd.read_sql(query1, con=db)
neg = list(df['Negara_ASEAN'])
pop = list(df['Populasi_Negara'])

x= neg
y= pop

# for a,b in zip(x,y):
#     plt.text(a,b, str(b), ha='center', size=6)
# plt.bar(x,y,color=['red','green','black','yellow','blue','lightblue','lightgreen','pink','magenta','purple','orange'])
# plt.title('Populasi Negara ASEAN')
# plt.xlabel('Negara')
# plt.ylabel('Populasi')
# plt.xticks(rotation=45, size=6)
# plt.grid(True)
# plt.show()

# fig = go.Figure(data= [go.Bar(
#     y = pop,
#     x = neg,
#     name = str(neg[0]),
#     text = pop,
#     textposition= 'auto',
#     marker_color= ['red','green','black','yellow','blue','lightblue','lightgreen','pink','magenta','purple','orange']
# )])

color = ['red','blue','green','yellow','lightgreen','lightblue','pink','purple','brown','lightgrey','orange']
plt.pie(
    y, labels=x, colors=color,
    startangle=360, counterclock=True,
    autopct='%1.1f%%',
    textprops={'color':'black'}
)
plt.show()