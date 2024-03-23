import plotly.express as px

def plot(df, x, y, labels, title):
    fig = px.line(df, x, y, labels=labels, title=title, width=1000, height=600)
    fig.update_layout(
        legend_title=''
    )
    
    fig.for_each_trace(lambda t: t.update(name = new[t.name]))
    return fig