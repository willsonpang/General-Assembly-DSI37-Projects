import streamlit as st
from datetime import date
import yfinance as yf
import nasdaqdatalink as ndl
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import numpy as np



START = "2013-07-26"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")

stocks = ("GME", "AMC", "TSLA", "META", "GM", "UBER", "RIOT", "AMD")
selected_stock = st.selectbox("Select dataset for prediction", stocks)

n_years = st.slider("Years of prediction:", 1, 4) #slider can choose to predict from 1 - 4 years
period = n_years * 365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace = True)
    return data

data_load_state = st.text("Load data...")
data = load_data(selected_stock)
data_load_state.text("Loading data...done!")

st.subheader('Raw data')
st.write(data.tail())

def calc_vwap():
    data["Typical_Price"] = (data["High"] + data["Low"] + data["Close"])/3
    data["VWAP"] = (np.cumsum(data["Volume"] * data["Typical_Price"]) / np.cumsum(data["Volume"])).round(2)

# def calc_vwap():
#     data['typical_price'] = (data['High'] + data['Low'] + data['Close']) / 3
#     data['tp_times_volume'] = data['typical_price'] * data['Volume']
#     data['cumulative_tp_times_volume'] = data['tp_times_volume'].cumsum()
#     data['cumulative_volume'] = data['Volume'].cumsum()
#     data['VWAP'] = data['cumulative_tp_times_volume'] / data['cumulative_volume'].round(2)
#     # data = data.drop(['typical_price', 'tp_times_volume', 'cumulative_tp_times_volume', 'cumulative_volume'], axis=1)

calc_vwap()


def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = data['Date'], y = data['Open'], name = 'stock_open'))
    fig.add_trace(go.Scatter(x = data['Date'], y = data['Close'], name = 'stock_close'))
    fig.layout.update(title_text = "Time Series Data", xaxis_rangeslider_visible = True)
    st.plotly_chart(fig)

plot_raw_data()

# Forecasting
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns = {"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods = period)
forecast = m.predict(future)

st.subheader('Forecast data')
st.write(forecast.tail())

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

st.subheader('Plots')
st.write('Plots of Forecast Data')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)



st.write('Plots of Forecast Components')
fig2 = m.plot_components(forecast)
st.write(fig2)