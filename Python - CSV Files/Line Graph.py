import pandas as pd
import plotly.express as px

airports = ['Dublin', 'Cork', 'Shannon', 'Knock', 'Kerry']

for airportName in airports:
    df = pd.read_csv(f"{airportName}Airport.csv")
    
    fig = px.line(df, x="Date", y="Passengers", color='Airport')
    fig.show() # Only to check the graph before saving
    
    '''fig_path = f"{airportName}_line_plot.html"
    fig.write_html(fig_path)
    print(f"{airportName} interactive line plot saved to {fig_path}")'''

'''
# For The Line Graph With All The Airports
df = pd.read_csv("OnlyAirports.csv")
    
fig = px.line(df, x="Date", y="Passengers", color='Airport')
    
fig_path = f"Airport_line_plot.html"
fig.write_html(fig_path)
print(f"Airport interactive line plot saved to {fig_path}")'''