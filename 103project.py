import pandas as pd
import plotly_express as px

df=pd.read_csv(r"C:\Users\ADMIN\Dropbox\My PC (DESKTOP-QH1TBQA)\Downloads\New folder (5)\Data-visualization-master\csv files\Copy+of+data+-+data.csv")
fig=px.scatter(df,x="date",y="cases",color="country")
fig.show()