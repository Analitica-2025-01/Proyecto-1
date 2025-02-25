import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Lista de estados y fuentes de anuncios
states = ['DC', 'IN', 'VA', 'WA', 'NY', 'CA', 'AZ', 'NC', 'TX', 'GA', 'FL', 'AL', 'MD', 'CO', 'NM', 'IL', 'TN', 'AK', 'MA', 'NJ', 'OR', 'DE', 'PA', 'IA', 'SC', 'MN', 'MI', 'KY', 'WI', 'OH', 'CT', 'RI', 'NV', 'UT', 'MO', 'OK', 'NH', 'NE', 'LA', 'ND', 'AR', 'KS', 'ID', 'HI', 'MT', 'VT', 'SD', 'WV', 'MS', 'ME', 'WY']
sources = ['RentLingo', 'Listanza', 'ListedBuy', 'RentDigs.com', 'GoSection8', 'RealRentals', 'RENTOCULAR', 'rentbits', 'Home Rentals', 'Real Estate Agent', 'RENTCafé', 'tenantcloud']

# Layout con formulario
layout = html.Div([
    html.H1("Predictor de Precios", style={'font-weight': 'bold', 'textAlign': 'center'}),
    html.Div(style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}, children=[
        html.Div([
            html.Img(src="/assets/apartamento2.png", style={'width': '100%', 'maxWidth': '500px', 'borderRadius': '10px'})
        ], style={'flex': '1', 'padding': '20px'}),
        html.Div(style={'flex': '1', 'padding': '20px'}, children=[
            
            html.Label("Número de Baños"),
            dcc.Input(id="bathrooms-input", type="number", min=0, placeholder="Ej. 2", style={'width': '100%'}),
            
            html.Label("Número de Habitaciones"),
            dcc.Input(id="bedrooms-input", type="number", min=0, placeholder="Ej. 3", style={'width': '100%'}),
            
            html.Label("Tiene foto"),
            dcc.Dropdown(
                id='has-photo-input',
                options=[
                    {'label': 'Sí', 'value': 'Sí'},
                    {'label': 'No', 'value': 'No'}
                ],
                placeholder="Selecciona una opción",
                style={'width': '100%'}
            ),
            
            html.Label("Se permiten mascotas"),
            dcc.Dropdown(
                id='pets-allowed-input',
                options=[
                    {'label': 'Sí', 'value': 'Sí'},
                    {'label': 'No', 'value': 'No'}
                ],
                placeholder="Selecciona una opción",
                style={'width': '100%'}
            ),
            
            html.Label("Tamaño (pies cuadrados)"),
            dcc.Input(id="square-feet-input", type="number", min=0, placeholder="Ej. 1200", style={'width': '100%'}),
            
            html.Label("Estado en que se ubica"),
            dcc.Dropdown(
                id='state-input',
                options=[{'label': state, 'value': state} for state in states],
                placeholder="Selecciona un estado",
                style={'width': '100%'}
            ),
            
            html.Label("Origen del anuncio"),
            dcc.Dropdown(
                id='source-input',
                options=[{'label': source, 'value': source} for source in sources],
                placeholder="Selecciona una fuente",
                style={'width': '100%'}
            ),
            
            html.Button("Calcular Precio", id="predict-button", style={
                'width': '100%', 'backgroundColor': '#5A3E91', 'color': 'white', 'padding': '10px',
                'border': 'none', 'borderRadius': '5px', 'marginTop': '20px'
            })
        ])
    ]),
    
    # Resultado del precio
    html.Div(
        "Valor del Apartamento: $0", id="predicted-price",
        style={'textAlign': 'center', 'color': '#5A3E91', 'fontWeight': 'bold', 'marginTop': '20px'}
    )
])