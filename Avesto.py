import pandas as pd

df = pd.read_csv('investment_products.csv')
print(df.head())

def build_chart(*categories, df=df, percentile=0.8, top_n=4):
    dt = df.copy()
    if categories:
        dt = dt[dt['Category'].isin(categories)]

    C = dt['priceStock'].mean()
    m = dt['maximumCapital'].quantile(percentile)
    q_dt = dt.copy().loc[dt['maximumCapital'] >= m]
    dt['score'] = dt.apply(lambda x: (x['maximumCapital'] / (x['maximumCapital'] + m) * x['priceStock']) + (m / (m + x['maximumCapital']) * C), axis=1)
    q_dt = dt.sort_values('score', ascending=False).head(top_n)

    # print(q_dt[['name', 'score']])

    return list(q_dt['name'])

print(build_chart("Agro", "Technology", percentile=0.8))




 






