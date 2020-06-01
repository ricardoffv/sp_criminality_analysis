import streamlit as st
import pandas as pd
import pydeck as pdk

data = pd.read_csv('./criminalidade_sp_2.csv')

st.title('Criminalidade em São Paulo')
st.markdown(
	"""
	A criminalidade é um problema recorrente no Brasil. 
	Buscamos sempre formas de diminuir esses índices e usando técnicas de Ciências de Dados conseguimos 
	entender melhor o que está acontecendo e gerar insights que direcionem ações capazes de diminuir os 
	índices de criminalidade. Como na localização das ocorrências abaixo.
	"""
)

st.sidebar.info('Foram carregdas {} linhas'.format(data.shape[0]))

if st.sidebar.checkbox('Ver dataset'):
	st.header('Raw Data')
	st.write(data)

data.time = pd.to_datetime(data.time)
selected_year = st.sidebar.slider('Selecione um ano', 2010, 2018, 2015)
data_selected = data[data.time.dt.year == selected_year]

st.map(data_selected)


st.markdown(
	"""
	Pode-se explorar, geograficamente, outros insights sobre os crimes ocorridos no estado de São Paulo,
	verficando o gráfico abaixo que, além de exibir a localização, destaca a incidência de crimes na mesma.
	"""
)

st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=-23.567145	,
        longitude=-46.648936,
        zoom=8,
        pitch=50
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=data_selected[['latitude', 'longitude']],
            get_position='[longitude,latitude]',
            auto_highlight=True,
            elevation_scale=50,
            pickable=True,
            elevation_range=[0, 3000],
            extruded=True,
            coverage=1
        )
    ],
))

