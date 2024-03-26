import os
from pandas import read_csv, DataFrame
from getGaugeData import getGaugeData

gauges = {}
directory = 'data/gauges'
for file in os.listdir(directory):
    code = os.path.split(file)[1][1:6]
    gauges[code] = getGaugeData(os.path.join(directory, file))

years = [i for i in range(1961, 2022)]

distanses = read_csv('data/distanses/volga.csv')
distanses['gauge'] = distanses['gauge'].astype(str)

table = DataFrame(columns=["year"] + distanses['gauge'].tolist())
print(table)

for year in years:
    arr = [None for i in range(0, len(distanses['gauge'].tolist()))]
    print(arr)
    table.loc[year] = arr

print(table)
"""
for gauge, df in gauges.items():
    if gauge in distanses['gauge'].tolist():
        for year in years:
            year_str = str(year)
            res = df[df['date'].dt.year == year]
            max_stage = res.loc[res['stage'] == res['stage'].max()]
            print(max_stage)
            max_stage_date = max_stage.iloc[0]['date']
            print(max_stage_date)
            table.loc[year] = max_stage_date

print(table)
"""