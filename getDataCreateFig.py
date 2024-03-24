from getDataFromCSV import dfFromCsv
from dailyPlot import plot

def getDataCreateFig(year = 1961):
    df = dfFromCsv('data/heps/{}.csv'.format(str(year)))
    fig = plot(df, 'date', ['common', 'diff'], {'date': 'Дата', 'value': 'Расход'}, title=year)
    return df, fig
