# -*- coding: utf-8 -*-

"""
"""

import dash
from dash import Dash
from dash import DiskcacheManager, CeleryManager, Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc


sidebar = html.Div(
    [
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"), html.Span("Home")],
                    href="/",
                    active="exact",
                ),
                #dbc.NavLink(
                    #...
                #),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="/about"), ),
    ],
    brand="vllm-chat",
    brand_href="#",
    color="primary",
    dark=True,
    style={"margin": 0, "height": "7vh",}
)
