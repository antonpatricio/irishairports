import pandas as pd
import plotly.express as px

df = pd.read_csv('OnlyAirports.csv')

fig = px.pie(df, values='Passengers', names='Airport')
fig.show()

'''fig_path = f"Airport_pie_plot.html"
fig.write_html(fig_path)
print(f"Interactive pie plot saved to {fig_path}")'''