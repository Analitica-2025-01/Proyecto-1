import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Cargar datos
file_path = 'datos_apartamentos_rent.csv'
df = pd.read_csv(file_path, encoding='cp1252', sep=';')
df = df.dropna(subset=['latitude', 'longitude', 'price'])

# Lista de estados (convertimos a lista para añadir la opción "Todo")
states = df['state'].dropna().unique().tolist()
states.insert(0, 'Todo')  # Agregamos una opción para mostrar todos

layout = html.Div([
    html.H1("Mapa Interactivo de Precios de Alquiler", style={'font-weight': 'bold', 'textAlign': 'center'}),
    dcc.Dropdown(
        id='state-filter',
        options=[{'label': s, 'value': s} for s in states],
        placeholder="Selecciona un estado",
        value='Todo'  # Valor por defecto
    ),
    dcc.Graph(id='map-graph')
])

def register_visualizacion_callbacks(app):
    @app.callback(
        Output('map-graph', 'figure'),
        [Input('state-filter', 'value')]
    )
    def update_map(selected_state):
        # Si el usuario selecciona "Todo" o no selecciona nada, usamos el dataset completo
        if selected_state == 'Todo' or not selected_state:
            filtered_df = df
            zoom = 2.5
            # Opcional: centro del mapa, por ejemplo, centrado en la media global
            center = dict(
                lat=df['latitude'].mean(),
                lon=df['longitude'].mean()
            )
        else:
            filtered_df = df[df['state'] == selected_state]
            # Acercamos un poco más el zoom
            zoom = 5
            # Centramos en la media de lat/lon de ese estado
            center = dict(
                lat=filtered_df['latitude'].mean(),
                lon=filtered_df['longitude'].mean()
            )
        
        fig = px.scatter_mapbox(
            filtered_df,
            lat="latitude",
            lon="longitude",
            color="price",
            size="price",
            hover_name="title",
            hover_data=["cityname", "state", "price", "square_feet", "bedrooms", "bathrooms"],
            color_continuous_scale="Plasma",
            size_max=20,
            zoom=zoom,
            center=center,
            mapbox_style="carto-positron"
        )
        return fig