import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Diccionario con tickers clasificados por sector
sectores = {
    "Financiero": ["VALO.BA", "SUPV.BA", "GGAL.BA", "BBAR.BA", "BMA.BA", "BHIP.BA", "BPAT.BA", "BYMA.BA", "GBAN.BA"],
    "Energía": ["PAMP.BA", "CEPU.BA", "EDN.BA", "TGNO4.BA", "TGSU2.BA", "TRAN.BA", "METR.BA", "LEDE.BA", "ROSE.BA", "YPFD.BA"],
    "Consumo": ["MOLI.BA", "AGRO.BA", "POLL.BA", "CARC.BA", "CADO.BA", "GARO.BA", "GRIM.BA"],
    "Materiales y Construcción": ["ALUA.BA", "TXAR.BA", "LOMA.BA", "CELU.BA", "MORI.BA", "HAVA.BA", "MOLA.BA", "LONG.BA", "FERR.BA", "CGPA2.BA", "BOLT.BA", "CTIO.BA", "INVJ.BA", "DYCA.BA"],
    "Telecomunicaciones y Tecnología": ["CVH.BA", "TECO2.BA", "COME.BA"],
    "Inmobiliario": ["IRSA.BA", "CRES.BA"],
    "Industria": ["FIPL.BA", "SECO2.BA", "SEMI.BA", "SAMI.BA", "GCDI.BA", "GCLA.BA", "OEST.BA"]
}

# Configuración de la aplicación en Streamlit
st.title('Evolución de Precios por Sector en la Bolsa Argentina')

# Seleccionar sector
sector = st.selectbox("Selecciona un sector", list(sectores.keys()))

# Seleccionar rango de fechas
start_date = st.date_input("Fecha de inicio", value=pd.to_datetime("2023-01-01"))
end_date = st.date_input("Fecha de fin", value=pd.to_datetime("2023-12-31"))

# Botón para generar el gráfico
if st.button("Generar gráfico"):
    # Obtener los tickers del sector seleccionado
    tickers_sector = sectores.get(sector, [])

    if not tickers_sector:
        st.write(f"No se encontraron tickers para el sector {sector}")
    else:
        # Descargar datos de precios para los tickers en el sector
        precios = yf.download(tickers_sector, start=start_date, end=end_date)['Adj Close']

        # Graficar la evolución de precios
        plt.figure(figsize=(14, 7))
        for ticker in precios.columns:
            plt.plot(precios[ticker], label=ticker)
        
        plt.title(f'Evolución de Precios en el Sector {sector}')
        plt.xlabel('Fecha')
        plt.ylabel('Precio Ajustado de Cierre')
        plt.legend()
        plt.grid(True)

        # Mostrar gráfico en Streamlit
        st.pyplot(plt)
