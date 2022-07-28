import yfinance as yf
import streamlit as st

st.write("""
# Santko
Aqui se muestra el precio **De cierre** Del Bitcoin en Dólares Americanos!
""")

#definir el ticker
tickerSymbol = 'BTC-USD'
#obtener datos
tickerData = yf.Ticker(tickerSymbol)
#obtener precios historicos
tickerDf = tickerData.history(period='1d', start='2019-2-1', end='2022-7-27')


st.write("""
## Precio de cierre
""")
st.line_chart(tickerDf.Close)
