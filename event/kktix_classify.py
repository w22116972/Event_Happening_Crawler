import pandas as pd
file_name = 'event/event/kktix_geo.csv'
df = pd.read_csv(file_name, sep=',', decimal=b'.')
category = [
    'Entertainment',
    'Food',
    'Sports',
    'Uncategorized',
    'Learning',
    'Outdoor',
    'Networking',
    'Gathering'
]
for i in category:
    df_cate = pd.DataFrame(df[df['category'] == i])
    if i == 'Uncategorized':
        cate = 'Other'
    elif i == 'Learning':
        cate = 'Education'
    elif i == 'Outdoor':
        cate = 'Health'
    elif i == 'Networking':
        cate = 'Business'
    else:
        cate = i
    df_cate.to_csv('event/event/{}.csv'.format(cate) , index=False)
