import plotly.express as px

def plot(df, x, y, labels, title):
    fig = px.line(df, x, y, labels=labels, title=title, width=1000, height=600)
    fig.update_layout(
        legend_title=''
    )
    newNames = {
        'common': 'Расход через водосбросы', 
        'diff': 'Расход через гидроагрегаты'
        }
    
    fig.for_each_trace(lambda t: t.update(name = newNames[t.name],
                                          legendgroup = newNames[t.name],
                                          hovertemplate = t.hovertemplate.replace(t.name, newNames[t.name])))
    fig.update_layout(showlegend=False)
    max_discharge = df['common'].max()

    max_discharge_dates = df.loc[df['common'] == df['common'].max()]
    first_max_discharge_date = max_discharge_dates.iloc[0]['date']

    fig.add_vline(
        x=first_max_discharge_date, 
        line_width=2, 
        line_dash="dash", 
        line_color="green")

    fig.add_hline(
        y=max_discharge, 
        line_width=2, 
        line_dash="dash", 
        line_color="green",
        annotation_text=str(max_discharge), 
        annotation_position="bottom right",
        annotation=dict(font_size=15))
    # """
    if 'flood' in df:
        flood_days = df.loc[df['flood'] == True]        
        fig.add_vrect(x0=flood_days.iloc[0]['date'],
                      x1=flood_days.iloc[-1]['date'], 
                      annotation_text="Половодье", annotation_position="top left",
                      fillcolor="green", opacity=0.1, line_width=0)
    
    if 'max_discharge' in df:
        max_discharge_days = df.loc[df['max_discharge'] == True]        
        fig.add_vrect(x0=max_discharge_days.iloc[0]['date'],
                      x1=max_discharge_days.iloc[-1]['date'], 
                      annotation_text="Макс.расход", annotation_position="top left",
                      fillcolor="green", opacity=0.25, line_width=0)
    # """
    return fig
