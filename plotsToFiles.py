from getDataCreateFig import getDataCreateFig

years = [i for i in range(1961, 2022)]

for i in years:
    df, fig = getDataCreateFig(i)
    fig.write_image('plots/heps/{}.png'.format(i))
