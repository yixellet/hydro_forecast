import os
from getGaugeData import getGaugeData

gauges = {}
directory = 'data/gauges'
for file in os.listdir(directory):
    code = os.path.split(file)[1][1:6]
    gauges[code] = getGaugeData(os.path.join(directory, file))

years = [i for i in range(1961, 2022)]

volga_gauges = ['77090', '77094', '77102', '77106', '77801', '77807', '77808', '77890', '77813']

for gauge, df in gauges.items():
    print(gauge)