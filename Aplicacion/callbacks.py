from dash.dependencies import Input, Output
from paginas import home, predictor, analizador, visualizacion

def register_callbacks(app):
    # Callback de navegación de páginas: cambia el layout según la URL
    @app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/visualizacion':
            return visualizacion.layout
        elif pathname == '/predictor':
            return predictor.layout
        elif pathname == '/analizador':
            return analizador.layout
        else:
            return home.layout
    
    # Registrar los callbacks específicos de visualizacion
    visualizacion.register_visualizacion_callbacks(app)