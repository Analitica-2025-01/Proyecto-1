from dash.dependencies import Input, Output, State
from paginas import home, predictor, analizador, visualizacion

# Coeficientes de regresión
coeficientes = {
    'state': {
        'AL': -190.30221306307013, 'AR': -370.4403539041502, 'AZ': -49.25890139158583, 'CA': 892.7361610725218,
        'CO': 206.9176807254088, 'CT': 191.4680613998342, 'DC': 882.3836940685518, 'DE': -188.25696865987788,
        'FL': 98.7811478714432, 'GA': -6.8985370739603695, 'HI': 975.3471274192361, 'IA': -260.38884221839317,
        'ID': 143.89452340868644, 'IL': 217.87336807443688, 'IN': -170.33678293667222, 'KS': -275.5625152418587,
        'KY': -240.63563511141558, 'LA': -245.35341879130155, 'MA': 865.4885809731095, 'MD': 331.8476244417451,
        'ME': 547.5188822397668, 'MI': -106.32938949022076, 'MN': 205.06233233738448, 'MO': -197.82504893279662,
        'MS': -336.3908743456227, 'MT': -8.861728137017426, 'NC': -111.67067646568528, 'ND': -343.23515083906466,
        'NE': -225.32533895009473, 'NH': 303.62933161088404, 'NJ': 608.0239401863716, 'NM': -103.85540380870255,
        'NV': -34.9299539624983, 'NY': 328.1771011431661, 'OH': -149.00235306484265, 'OK': -179.03758932998076,
        'OR': 284.4275083280411, 'PA': 95.40036018395233, 'RI': 328.4005212753681, 'SC': -170.83221234779384,
        'SD': -322.55370226981734, 'TN': 91.37773716943826, 'TX': 33.59760261696236, 'UT': -2.7766625128071087,
        'VA': 235.91611937365553, 'VT': 257.45731946675994, 'WA': 501.7552424238915, 'WI': 27.630972875506174,
        'WV': -355.5815158886598, 'WY': -496.1775236061492
    },
    'source': {
        'Home Rentals': -13.641679769167023, 'Listanza': 399.3628848628638, 'ListedBuy': 6.932657836599033,
        'RENTCafé': -37.558064669514316, 'RENTOCULAR': 190.00664522625007, 'RealRentals': 355.13454002825785,
        'RentDigs.com': 145.96722720154636, 'RentLingo': 190.61322845703754, 'rentbits': -134.52244774223902,
        'tenantcloud': -298.36842478585237
    },
    'bathrooms': 102.63448578281232,
    'bedrooms': 7.70136430758655,
    'has_photo': -36.24553830418691,
    'pets_allowed': 13.970376659251972,
    'square_feet': 0.5673927285973768
}

def register_callbacks(app):
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

    visualizacion.register_visualizacion_callbacks(app)
        # Registrar el callback de analizador
    analizador.register_analizador_callbacks(app)

    @app.callback(
        Output("predicted-price", "children"),
        [Input("predict-button", "n_clicks")],
        [
            State("bathrooms-input", "value"),
            State("bedrooms-input", "value"),
            State("has-photo-input", "value"),
            State("pets-allowed-input", "value"),
            State("square-feet-input", "value"),
            State("state-input", "value"),
            State("source-input", "value")
        ]
    )
    def predict_price(n_clicks, bathrooms, bedrooms, has_photo, pets_allowed, square_feet, state, source):
        if n_clicks == 0:
            return ""

        # Precio base
        base_price = 0

        # Ajustes según los coeficientes
        if bathrooms:
            base_price += bathrooms * coeficientes['bathrooms']
        if bedrooms:
            base_price += bedrooms * coeficientes['bedrooms']
        if has_photo:
            base_price += coeficientes['has_photo'] if has_photo == 'Sí' else 0
        if pets_allowed:
            base_price += coeficientes['pets_allowed'] if pets_allowed == 'Sí' else 0
        if square_feet:
            base_price += square_feet * coeficientes['square_feet']
        if state:
            base_price += coeficientes['state'].get(state, 0)
        if source:
            base_price += coeficientes['source'].get(source, 0)

        return f"El precio estimado es: ${base_price:.2f}"