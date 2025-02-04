# -*- coding: utf-8 -*-

"""
"""
from flask import Flask, jsonify
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

# create Flask & Dash server
server = Flask(__name__)
app = Dash(
    __name__,
    server = server,
    external_stylesheets=[dbc.themes.SANDSTONE, dbc.icons.FONT_AWESOME] + dmc.styles.ALL,
    #use_pages=True,
    #pages_folder="pages",
    #assets_folder="dashboard/assets",
    #requests_pathname_prefix='/dashboard/'
)
app.title = "vllm-chat"
#app.config.suppress_callback_exceptions = True

#server = app.server

# ----------------- endpoints
#view_func = lambda x : 
#app._add_url('', view_func, methods=('GET',))

@server.route("/about")
def about_page():
    #page = dcc.Markdown(
        #'''
        ## About page
        #'''
    #)
    page = f'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>vllm-chat about</title>
            </head>
            <body>
                <h1>About page</h2>
                <div id="about-text">
                        Simple app providing chat to comunicate with vLLM server.
                </div>
                <footer>
                <p>Authors: Konrad Kobuszewski, Paulina Kobuszewska</p>
                <p><a href="mailto:konrad.kobuszewski93@gmail.com">konrad.kobuszewski93@gmail.com</a></p>
                </footer>
            </body>
        </html>
    '''
    return page



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
                    style={
                        "width": 200,
                        "margin": ["1%" "5%" "5%" "5%"],
                        },
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
            className="content"
        ),
    ])
)

# TODO: dmc not working????

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8050,
    )

