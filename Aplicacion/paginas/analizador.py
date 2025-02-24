import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([
    html.H2("Analizador de Títulos y Descripciones", style={'textAlign': 'center', 'fontWeight': 'bold'}),
    html.Div([
        # Columna de entradas y resultados
        html.Div([
            html.P("Ingresa el título del apartamento:", style={'textAlign': 'center'}),
            dcc.Textarea(
                id='title-input',
                placeholder="Escribe el título aquí...",
                style={'width': '100%', 'height': '80px', 'padding': '10px', 'fontSize': '16px'}
            ),
            html.Br(),
            html.P("Ingresa la descripción del apartamento:", style={'textAlign': 'center'}),
            dcc.Textarea(
                id='description-input',
                placeholder="Escribe la descripción aquí...",
                style={'width': '100%', 'height': '200px', 'padding': '10px', 'fontSize': '16px'}
            ),
            html.Br(),
            html.Button("Analizar", id='analyze-button', n_clicks=0, 
                        style={
                            'display': 'block', 'margin': '20px auto', 
                            'padding': '10px 20px', 'backgroundColor': '#5A3E91', 
                            'color': 'white', 'border': 'none', 'borderRadius': '5px'
                        }),
            html.Div(id='analysis-output', 
                     style={
                         'marginTop': '20px', 'textAlign': 'center', 
                         'fontWeight': 'bold', 'fontSize': '18px'
                     })
        ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '10px'}),
        # Columna de imagen con palabra más utilizadas
        html.Div([
            html.Img(src="/assets/texto.png", style={'width': '100%', 'maxWidth': '400px', 'display': 'block', 'margin': 'auto'}),
            html.P("Palabras mas utilizadas en descripciones", style={'textAlign': 'center', 'fontWeight': 'bold', 'marginTop': '10px'})
        ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '10px'})
    ], style={'maxWidth': '800px', 'margin': 'auto', 'padding': '20px'})
])