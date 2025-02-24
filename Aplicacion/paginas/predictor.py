from dash import dcc, html

layout = html.Div([
    # Título
    html.H1("Predictor de Precios", style={'textAlign': 'center', 'color': '#5A3E91'}),
    
    # Contenedor principal
    html.Div(style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}, children=[
        
        # Imagen del apartamento
        html.Div([
            html.Img(src="/assets/apartamento2.png", style={'width': '100%', 'maxWidth': '500px', 'borderRadius': '10px'})
        ], style={'flex': '1', 'padding': '20px'}),
        
        # Formulario de entrada
        html.Div(style={'flex': '1', 'padding': '20px'}, children=[
            
            html.Label("Número de Baños"),
            dcc.Input(id="bathrooms-input", type="number", min=0, placeholder="Ej. 2", style={'width': '100%'}),
            
            html.Label("Número de Habitaciones"),
            dcc.Input(id="bedrooms-input", type="number", min=0, placeholder="Ej. 3", style={'width': '100%'}),
            
            html.Label("Tiene foto (sí/no)"),
            dcc.Input(id="has-photo-input", type="text", placeholder="Ej. sí", style={'width': '100%'}),
            
            html.Label("Se permiten mascotas(sí/no)"),
            dcc.Input(id="pets-allowed-input", type="text", placeholder="Ej. sí/no", style={'width': '100%'}),
            
            html.Label("Tamaño (pies cuadrados)"),
            dcc.Input(id="square-feet-input", type="number", min=0, placeholder="Ej. 1200", style={'width': '100%'}),
            
            html.Label("Estado en que se ubica"),
            dcc.Input(id="state-input", type="text", placeholder="Ej. NY", style={'width': '100%'}),
            
            html.Label("Origen del anuncio"),
            dcc.Input(id="source-input", type="text", placeholder="Ej. Craigslist", style={'width': '100%'}),
            
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
