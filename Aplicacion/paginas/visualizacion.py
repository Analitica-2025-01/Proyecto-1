import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Cargar datos
file_path = 'df_william.csv'
df = pd.read_csv(file_path, encoding='cp1252', sep=',')

# Lista de estados con la opción "Todo"
states = df['state'].dropna().unique().tolist()
states.insert(0, 'Todo')

# Layout
layout = html.Div([
    html.H1("Mapa Interactivo de Precios de Alquiler", style={'font-weight': 'bold', 'textAlign': 'center'}),

    # Filtro de estado
    dcc.Dropdown(
        id='state-filter',
        options=[{'label': s, 'value': s} for s in states],
        placeholder="Selecciona un estado",
        value='Todo'
    ),

    # Mapa interactivo
    dcc.Graph(id='map-graph'),

    # Métricas principales
    html.Div([
        html.P("Precio Promedio: ", style={'font-weight': 'bold'}),
        html.Span(id='precio-promedio'),
        html.Br(),
        html.P("Baños Promedio: ", style={'font-weight': 'bold'}),
        html.Span(id='banos-promedio'),
        html.Br(),
        html.P("Habitaciones Promedio: ", style={'font-weight': 'bold'}),
        html.Span(id='habitaciones-promedio'),
    ], style={'padding': '10px'}),

    # Contenedores para Top Apartamentos y Top Sitios
    html.Div([
        html.Div([
            html.H4("Top Apartamentos"),
            html.Ul(id="top-apartamentos"),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'border': '1px solid lightgray'}),

        html.Div([
            html.H4("Top Sitios"),
            html.Ul(id="top-sitios"),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'border': '1px solid lightgray'}),
    ], style={'display': 'flex', 'justify-content': 'space-between'}),

    # Gráficos circulares
    html.Div([
        dcc.Graph(id='grafico-mascotas', style={'width': '45%', 'display': 'inline-block'}),
        dcc.Graph(id='grafico-fotos', style={'width': '45%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justify-content': 'space-between'})
])

# Callbacks
def register_visualizacion_callbacks(app):
    @app.callback(
        Output('map-graph', 'figure'),
        [Input('state-filter', 'value')]
    )
    def update_map(selected_state):
        if selected_state == 'Todo' or not selected_state:
            filtered_df = df
            zoom = 2.5
            center = dict(lat=df['latitude'].mean(), lon=df['longitude'].mean())
        else:
            filtered_df = df[df['state'] == selected_state]
            zoom = 7
            center = dict(lat=filtered_df['latitude'].mean(), lon=filtered_df['longitude'].mean())

        fig = px.scatter_mapbox(
            filtered_df,
            lat="latitude",
            lon="longitude",
            color="price",
            size="price",
            hover_name="title",
            hover_data=["cityname", "state", "price", "square_feet", "bedrooms", "bathrooms"],
            color_continuous_scale="Plasma",
            size_max=15,
            zoom=zoom,
            center=center,
            mapbox_style="carto-positron"
        )
        return fig

    @app.callback(
        [Output('precio-promedio', 'children'),
         Output('banos-promedio', 'children'),
         Output('habitaciones-promedio', 'children')],
        [Input('state-filter', 'value')]
    )
    def update_metrics(selected_state):
        filtered_df = df if selected_state == 'Todo' else df[df['state'] == selected_state]
        precio_prom = filtered_df['price'].mean()
        banos_prom = filtered_df['bathrooms'].mean()
        habitaciones_prom = filtered_df['bedrooms'].mean()
        return f"${precio_prom:,.0f}", f"{banos_prom:.1f}", f"{habitaciones_prom:.1f}"

    @app.callback(
        Output('top-apartamentos', 'children'),
        [Input('state-filter', 'value')]
    )
    def update_top_apartments(selected_state):
        filtered_df = df if selected_state == 'Todo' else df[df['state'] == selected_state]
        top_apts = filtered_df.nlargest(4, 'price')[['title', 'price']].values.tolist()
        return [html.Li(f"{title} - ${price:,.0f}") for title, price in top_apts]

    @app.callback(
        Output('top-sitios', 'children'),
        [Input('state-filter', 'value')]
    )
    def update_top_sites(selected_state):
        filtered_df = df if selected_state == 'Todo' else df[df['state'] == selected_state]
        top_sites = filtered_df['cityname'].value_counts().head(4).index.tolist()
        return [html.Li(site) for site in top_sites]

    @app.callback(
        Output('grafico-mascotas', 'figure'),
        [Input('state-filter', 'value')]
    )
    def update_pets_chart(selected_state):
        filtered_df = df if selected_state == 'Todo' else df[df['state'] == selected_state]
        pets_count = filtered_df['pets_allowed'].value_counts()
        fig = px.pie(
            names=pets_count.index.map(lambda x: "Sí" if x == 1 else "No"),
            values=pets_count.values,
            title="Permiten Mascotas"
        )
        return fig

    @app.callback(
        Output('grafico-fotos', 'figure'),
        [Input('state-filter', 'value')]
    )
    def update_photos_chart(selected_state):
        filtered_df = df if selected_state == 'Todo' else df[df['state'] == selected_state]
        photos_count = filtered_df['has_photo'].replace({'Thumbnail': 'Yes'}).value_counts()
        fig = px.pie(
            names=photos_count.index,
            values=photos_count.values,
            title="Tienen Foto"
        )
        return fig