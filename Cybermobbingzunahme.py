import streamlit as st
import pandas as pd
import altair as alt

st.header("Cybermobbing nimmt zu")
st.subheader("Anteil der betroffenen Schüler_innen zwischen acht und 21 Jahren 2017 und im Corona-Jahr 2020")

source = pd.DataFrame({
        'Anteil(%)': [12.7, 17.3],
        'Jahr': ['2017', '2020']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Jahr:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=6000+ Eltern, Lehrkräfte, Schülerinnen und Schüler in Deutschland; Feb. - Nov. 2020
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Bündnis gegen Cybermobbing/TK")