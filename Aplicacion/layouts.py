import dash_html_components as html
import dash_bootstrap_components as dbc

navbar = dbc.Navbar(
    dbc.Container([
        html.A(
            dbc.Row([
                dbc.Col(dbc.NavbarBrand("🏢Inmobiliaria de los Andes", className="ms-2",href="/home")),
            ], align="center", className="g-0"),
            href="#",
            style={"textDecoration": "none"}
        ),
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Visualización de Apartamentos", href="/visualizacion")),
            dbc.NavItem(dbc.NavLink("Predictor de Precios", href="/predictor")),
            dbc.NavItem(dbc.NavLink("Analizador de Descripciones", href="/analizador")),
        ], className="ml-auto", navbar=True),
    ]),
    color="dark",
    dark=True,
    className="navbar-custom",
)
