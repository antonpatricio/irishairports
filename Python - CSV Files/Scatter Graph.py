import pandas as pd
import plotly.express as px

airports = ['Dublin', 'Cork', 'Shannon', 'Knock', 'Kerry']

for airportName in airports:
    df = pd.read_csv(f"{airportName}Airport.csv")
    
    fig = px.scatter(df, x="Passengers", y="Date", color="Airport", size="Passengers", hover_data=["Date"])
    fig.show() # Only to check the graph before saving
    
    '''fig_path = f"{airportName}_scatter_plot.html"
    fig.write_html(fig_path)
    print(f"{airportName} interactive scatter plot saved to {fig_path}")'''