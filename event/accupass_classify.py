import pandas as pd

file_name = '/Users/ender/Documents/mit-city/event_density_map/event/event/accupass.csv'
df = pd.read_csv(file_name, sep=',', decimal=b'.')
category = [
    'Entertainment',
    'Food',
    'Sports',
    'Education',
    'Business',
    'Health',
    'Charity',
    'Technology'
]
arts_df = pd.DataFrame(df[df['cate'] == 'Arts'])
pho_df = pd.DataFrame(df[df['cate'] == 'Photography'])
fash_df = pd.DataFrame(df[df['cate'] == 'Fashion'])
arts_df.append([pho_df, fash_df]).to_csv('Arts.csv', index=False)

other_df = pd.DataFrame(df[df['cate'] == 'Other'])
trav_df = pd.DataFrame(df[df['cate'] == 'Travel'])
other_df.append(trav_df).to_csv('Other.csv', index=False)

for cate in category:
    cate_df = pd.DataFrame(df[df['cate'] == cate]).to_csv('{}.csv'.format(cate), index=False)

