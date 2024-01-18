import pandas as pd

df = pd.read_csv('table2.csv')

# df['peso'] = df['peso'].apply(lambda x: x+'.0')
print(df)
# for num in s:
#     if str(num).isnumeric():
#         continue
#     else:
#         print(f'{s} is not numeric')