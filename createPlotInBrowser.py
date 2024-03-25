from getDataFromCSV import dfFromCsv
from dailyPlot import plot
from app import app

year = 1979

df = dfFromCsv('data/heps/{}.csv'.format(str(year)))

fig = plot(df, 'date', ['common', 'diff'], {'date': 'Дата', 'value': 'Расход'}, title=year)

app(fig)
