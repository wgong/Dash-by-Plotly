"""
https://www.youtube.com/watch?v=_b2KXL0wHQg&list=PLh3I780jNsiTXlWYiNWjq2rBgg3UsL1Ub&index=1
"""

import pandas as pd
import plotly.express as px
dfb = pd.read_csv("bird-window-collision-death.csv")

# df = px.data.tips()
fig = px.pie(dfb, values='Deaths', names='Bldg #', color="Side", hole=0.3)
fig.update_traces(textinfo="label+percent", insidetextfont=dict(color="white"))
fig.update_layout(legend={"itemclick":False})
fig.show()

fig.write_image("images/fig1.png")