from pandas import read_csv, to_datetime

def dfFromCsv(file):
    data = read_csv(file, names=['date', 'common', 'spillway'])
    # data['date'] = to_datetime(data['date'])
    data['date'] = data['date'].astype("datetime64[ns]")
    print(data.dtypes)
    print(data.head)
    return data

if __name__ == "__main__":
    dfFromCsv('data/heps/1979.csv')