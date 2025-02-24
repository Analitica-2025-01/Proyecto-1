import dash_html_components as html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("¡Bienvenido al sistema Inmobiliario de La Inmobiliaria de los Andes!", className="title-text mb-4"),
            html.P("Selecciona una opción para continuar", className="subtitle-text"),
            dbc.Button("Visualización de Apartamentos", color="primary", className="custom-button mb-2", href="/visualizacion"),
            dbc.Button("Predictor de Precios", color="primary", className="custom-button mb-2", href="/predictor"),
            dbc.Button("Analizador de Descripciones", color="primary", className="custom-button", href="/analizador"),
        ], width=5, className="left-section"),
        dbc.Col([
            html.Img(src="/assets/apartamento.jpg", className="image-container")
        ], width=7),
    ], align="center", className="content-row mt-4"),
])
