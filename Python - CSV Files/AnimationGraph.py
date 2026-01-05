import pandas as pd
import plotly.express as px

df = pd.read_csv("OnlyAirports.csv")

fig = px.bar(df, x="Airport", y="Passengers", color="Airport", animation_frame="Date", animation_group="Airport", range_y=[0,4000000])

fig.show() # Only to check the graph before saving

'''fig_path = f"Airport_animation_plot.html"
fig.write_html(fig_path)
print(f"Airport interactive animation plot saved to {fig_path}")'''