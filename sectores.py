import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Diccionario con tickers clasificados por sector
sectores = {
    "Bienes de consumo duraderos": ["DOME.BA", "LONG.BA"],
    "Comercio minorista": ["PATA.BA", "REGE.BA"],
    "Comunicaciones": ["BOLT.BA", "CVH.BA", "TECO2.BA"],
    "Consumibles perecederos": ["GRIM.BA", "HAVA.BA", "MOLI.BA"],
    "Fabricación de productos": ["AGRO.BA", "FERR.BA", "MIRG.BA"],
    "Finanzas": ["BBAR.BA", "BHIP.BA", "BMA.BA", "BPAT.BA", "BYMA.BA", "CADOC.BA", "CTIO.BA", "GCDI.BA", "GGAL.BA", "MTRM.BA", "SUPV.BA", "VALO.BA"],
    "Industrias de proceso": ["CELU.BA", "CRES.BA", "INTR.BA", "LEDE.BA", "MOLA.BA", "MORI.BA", "RIGO.BA", "SAMI.BA", "SEMI.BA"],
    "Minerales energéticos": ["YPFD.BA"],
    "Minerales no energéticos": ["HARG.BA", "LOMA.BA", "TXAR.BA"],
    "Servicios al consumidor": ["GCLA.BA"],
    "Servicios de distribución": ["INVJ.BA"],
    "Servicios industriales": ["COME.BA", "DYCA.BA", "GBAN.BA", "OEST.BA", "POLL.BA", "TGNO4.BA"],
    "Servicios públicos": ["CAPX.BA", "CECO2.BA", "CEPU.BA", "CGPA2.BA", "DGCE.BA", "EDN.BA", "METR.BA", "PAMP.BA", "TGSU2.BA", "TRAN.BA"],
    "Servicios tecnológicos": ["GAMIB.BA"],
    "Tecnologías sanitarias": ["RICHL.BA", "ROSE.BA"],
    "Transporte": ["AUSO.BA", "CARC.BA"]
}

# Configuración de la aplicación en Streamlit
st.title('Evolución de Precios por Sector en la Bolsa Argentina')

# Seleccionar sector
sector = st.selectbox("Selecciona un sector", list(sectores.keys()))

# Obtener los tickers del sector seleccionado
tickers_sector = sectores.get(sector, [])

# Seleccionar múltiples tickers dentro del sector o "Todos"
tickers_seleccionados = st.multiselect(
    "Selecciona uno o más tickers o 'Todos'",
    ["Todos"] + tickers_sector,
    default="Todos"
)

# Seleccionar rango de fechas
start_date = st.date_input("Fecha de inicio", value=pd.to_datetime("2023-01-01"))
end_date = st.date_input("Fecha de fin", value=pd.to_datetime("2023-12-31"))

# Botón para generar el gráfico
if st.button("Generar gráfico"):
    # Si se selecciona "Todos", graficar todos los tickers del sector
    if "Todos" in tickers_seleccionados:
        precios = yf.download(tickers_sector, start=start_date, end=end_date)['Adj Close']
    else:
        precios = yf.download(tickers_seleccionados, start=start_date, end=end_date)['Adj Close']

    # Graficar la evolución de precios
    plt.figure(figsize=(14, 7))

    # Verificación si es un solo ticker (Serie)
    if isinstance(precios, pd.Series):
        plt.plot(precios, label=tickers_seleccionados[0])
    else:
        for ticker in precios.columns:
            plt.plot(precios[ticker], label=ticker)

    plt.title(f'Evolución de Precios en el Sector {sector}')
    plt.xlabel('Fecha')
    plt.ylabel('Precio Ajustado de Cierre')
    plt.legend()
    plt.grid(True)

    # Mostrar gráfico en Streamlit
    st.pyplot(plt)
