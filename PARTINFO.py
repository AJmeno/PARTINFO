import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Fetch the EURUSD data
# (Replace this with your data fetching logic)
df = pd.read_csv('eurusd_data.csv')

# Create the Streamlit app
st.set_page_config(page_title="EURUSD Dashboard")
st.title("EURUSD Dashboard")

# Display the EURUSD chart
fig = go.Figure(data=[go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close']
)])
fig.update_layout(xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)
