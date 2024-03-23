from pandas import read_csv

def dfFromCsv(file):
    return read_csv(file, names=['date', 'common', 'spillway'])