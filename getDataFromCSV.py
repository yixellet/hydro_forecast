from pandas import read_csv

def dfFromCsv(file):
    data = read_csv(file, names=['date', 'common', 'spillway', 'flood', 'max_discharge'])
    data['date'] = data['date'].astype("datetime64[ns]")
    data['diff'] = data['common'] - data['spillway']
    return data

if __name__ == "__main__":
    dfFromCsv('data/heps/1979.csv')