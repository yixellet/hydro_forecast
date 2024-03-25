from pandas import read_csv

def getGaugeData(file):
    data = read_csv(file)
    data['date'] = data['date'].astype("datetime64[ns]")
    return data

if __name__ == "__main__":
    print(getGaugeData('data/gauges/s77808.csv'))