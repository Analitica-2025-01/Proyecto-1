import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import joblib

# Cargar el modelo y el vectorizador (pkl)
model_randomForest = joblib.load("modelo_rf.pkl")
tf_idf_vectorizer = joblib.load("vectorizador_tfidf.pkl")

def predecir_precio(nuevos_textos, vectorizer, modelo):
    # Transformar los textos de entrada con el mismo vectorizador TF-IDF
    X_nuevo = vectorizer.transform(nuevos_textos)
    # Predecir el precio
    precio_predicho = modelo.predict(X_nuevo)
    return precio_predicho

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
            html.Button(
                "Analizar",
                id='analyze-button',
                n_clicks=0,
                style={
                    'display': 'block', 'margin': '20px auto',
                    'padding': '10px 20px', 'backgroundColor': '#5A3E91',
                    'color': 'white', 'border': 'none', 'borderRadius': '5px'
                }
            )
        ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '10px'}),

        # Columna de imagen y del resultado de precio
        html.Div([
            html.Img(
                src="/assets/texto.png",
                style={'width': '100%', 'maxWidth': '400px', 'display': 'block', 'margin': 'auto'}
            ),
            html.P(
                "Palabras mas utilizadas en descripciones",
                style={'textAlign': 'center', 'fontWeight': 'bold', 'marginTop': '10px'}
            ),
            # Aquí agregamos la sección para mostrar el precio
            html.Div(
                id='price-output',
                style={
                    'marginTop': '20px',
                    'textAlign': 'center',
                    'fontWeight': 'bold',
                    'fontSize': '18px'
                }
            )
        ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '10px'})
    ], style={'maxWidth': '800px', 'margin': 'auto', 'padding': '20px'})
])

def register_analizador_callbacks(app):
    @app.callback(
        Output('price-output', 'children'),
        [Input('analyze-button', 'n_clicks')],
        [State('title-input', 'value'), State('description-input', 'value')]
    )
    def analizar_texto(n_clicks, title, description):
        if n_clicks > 0 and title and description:
            # Unimos título y descripción para predecir (o puedes usar cada uno por separado)
            nuevos_textos = [title + " " + description]

            # Llamamos a la función que predice el precio
            precios_estimados = predecir_precio(nuevos_textos, tf_idf_vectorizer, model_randomForest)
            precio = precios_estimados[0]  # Solo un texto en la lista

            # Texto de salida debajo de la imagen
            price_text = f"Precio estimado: ${precio:.2f}"

            return price_text
        # Si no hay clics o faltan campos, mostramos vacío
        return "Precio estimado: "