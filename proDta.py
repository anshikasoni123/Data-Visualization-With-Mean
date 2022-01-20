import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data3.csv")
# student_df = df.loc[df['student_id']=='TRL_imb']
mean1 = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

fig = px.scatter(mean1,x="student_id",y="level",color = "attempt",size = "attempt")
fig.show()