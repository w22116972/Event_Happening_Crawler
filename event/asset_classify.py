import pandas as pd

file_name = '2017_buy_geo.csv'
df = pd.read_csv(file_name, sep=',', decimal=b'.')

category = [
    '住家用',
    '商業用',
    '停車空間',
    '住工用',
    '工業用'
]

df_other = pd.DataFrame(df[df['主要用途'] == '見使用執照'])
df_other.append(pd.DataFrame(df[df['主要用途'] == '見其他登記事項']))
df_other.to_csv('其他_buy.csv', index=False)


for i in category:
    df_cate = pd.DataFrame(df[df['主要用途'] == i])
    df_cate.to_csv('{}_buy.csv'.format(i) , index=False)