# -*- coding: utf-8 -*-

"""
"""

import dash
from dash import Dash
from dash import DiskcacheManager, CeleryManager, Input, Output, callback, html, dcc, \
                 clientside_callback, _dash_renderer
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

import dashboard
import dashboard.bars
import dashboard.chatbox

# import system variables
import dotenv
dotenv.load_dotenv()

_dash_renderer._set_react_version("18.2.0")

# create Dash server
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SANDSTONE, dbc.icons.FONT_AWESOME] + dmc.styles.ALL,
    #use_pages=True,
    #pages_folder="dashboard/pages",
    #assets_folder="dashboard/assets",
    #requests_pathname_prefix='/dashboard/'
)
app.title = "vllm-chat"
#app.config.suppress_callback_exceptions = True

server = app.server

clientside_callback(
    """
    function updateLoadingState(n_clicks) {
        return true
    }
    """,
    Output("loading-button", "loading", allow_duplicate=True),
    Input("loading-button", "n_clicks"),
    prevent_initial_call=True,
)


app.layout = dmc.MantineProvider(
    html.Div([
    dashboard.bars.navbar,
        html.Div([
                #dashboard.bars.sidebar,
                #dash.page_container
                #dashboard.chatbox.chatbox
                dmc.Select(
                    id="model-select",
                    data=["DeepSeek"], # <---------- TODO: here put models
                    value="DeepSeek",
                    style={"width": 200},
                    searchable=True,
                    #icon=DashIconify(icon="radix-icons:magnifying-glass"),
                    rightSection=DashIconify(icon="radix-icons:chevron-down"),
                ),
                dashboard.chatbox.chat_history,
                dmc.Textarea(
                    id="input-textarea",
                    placeholder="Enter your prompt here.",
                    autosize=False,
                    radius='md',
                    minRows=2,
                    maxRows=2,
                ),
                dmc.Button("Submit prompt to LLM", id="loading-button"),
            ],
            className="content",
        ),
    ])
)

# TODO: dmc not working????

if __name__ == "__main__":
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port=8050,
    )

