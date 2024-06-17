

import pandas as pd

def process(df):
    feb_s = pd.Timestamp('2024-02-01')
    feb_e = pd.Timestamp('2024-02-29')

    df['start'] = pd.to_datetime(df['timestamp'], unit='s')
    df['end'] = df['start'] + pd.to_timedelta(df['billing_period'] - 1, unit='D')
    df['profit'] = df['billing_total_price_usd'] / df['billing_period']

    dop = df[(df['end'] >= feb_s) & (df['start'] <= feb_e)]
    dop['start_in_feb'] = dop['start'].apply(lambda x: max(x, feb_s))
    dop['end_in_feb'] = dop['end'].apply(lambda x: min(x, feb_e))
    dop['days_in_feb'] = (dop['end_in_feb'] - dop['start_in_feb']).dt.days + 1
    dop['feb_pr'] = dop['days_in_feb'] * dop['profit']

    total = dop.groupby('user_id')['feb_pr'].sum()
    main_sum = round(total.nlargest(3).sum(), 2)
    print(df)
    print(dop)
    return main_sum
df = pd.read_csv("sample_1.csv")
print(process(df))
