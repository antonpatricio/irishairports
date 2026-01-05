import pandas as pd
import plotly.express as px

airports = ['Dublin', 'Cork', 'Shannon', 'Knock', 'Kerry']

for airportName in airports:
    df = pd.read_csv(f"{airportName}Airport.csv")
    
    fig = px.bar(df, x='Date', y='Passengers', color='Airport')
    fig.show() # Only to check the graph before saving
    
    '''fig_path = f"{airportName}_bar_plot.html"
    fig.write_html(fig_path)
    print(f"{airportName} interactive bar plot saved to {fig_path}")'''