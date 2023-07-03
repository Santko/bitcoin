import yfinance as yf
import streamlit as st

st.write("""
# Analisis Personal en Bolivia, solo para fines de Referencia, 
debido a que la negociacion de Criptoactivos, esta tipificada
delito financiero
Aqui se muestra el precio **De cierre** Del Bitcoin en Dólares Americanos!
""")

#definir el ticker
tickerSymbol = 'BTC-USD'
#obtener datos
tickerData = yf.Ticker(tickerSymbol)
#obtener precios historicos
tickerDf = tickerData.history(period='1d', start='2022-2-1', end='2023-6-30')


st.write("""
## Precio de cierre
""")
st.line_chart(tickerDf.Close)
