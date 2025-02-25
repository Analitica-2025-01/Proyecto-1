import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from callbacks import register_callbacks  # Registramos callbacks luego
from layouts import navbar  # Tu navbar, si la usas

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, "/assets/style.css"],
    suppress_callback_exceptions=True
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

# Registramos todos los callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)