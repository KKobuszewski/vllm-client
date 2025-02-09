# -*- coding: utf-8 -*-

"""
"""
import argparse
import asyncio

from flask import Flask, jsonify
import dash
import dash.exceptions
from dash import Dash
from dash import DiskcacheManager, CeleryManager, Input, Output, State, \
                 clientside_callback, callback, html, dcc, _dash_renderer
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

import client
import client.vllm_connector
import dashboard
import dashboard.elements

# import system variables
import dotenv
dotenv.load_dotenv()

_dash_renderer._set_react_version("18.2.0")

# create Flask & Dash server
#server = Flask(__name__) # can be passed to Dash(__name__, server=server)
app = Dash(
    'vllm-chat',
    #server = server,
    external_stylesheets=[dbc.themes.SANDSTONE, dbc.icons. FONT_AWESOME] + dmc.styles.ALL,
    #use_pages=True,
    #pages_folder="pages",
    #assets_folder="dashboard/assets",
    #requests_pathname_prefix='/dashboard/'
)
app.title = "vllm-chat"
#app.config.suppress_callback_exceptions = True


# ------------------------ vllm-server --------------------------------

vllm_connector = None # global 'handle' to vllmConnector (to be initiated in __main__ if clause)


# ------------------------ endpoints --------------------------------

# TODO: Model selection (dashboard.elements.model_selection) not working properly.
# https://github.com/plotly/dash/issues/214
# https://community.plotly.com/t/how-to-add-restful-api-endpoints-to-a-dash-app/27162/5
# https://community.plotly.com/t/apis-on-dash-server/30966/5
# NOTE: There's probably another way do add endpoint to Dash app
#app._add_url("/about", about_page, methods=('GET',))
# see: https://github.com/plotly/dash/blob/41632fb359cb01c0594d7024a98e6a7f6258a02a/dash/dash.py#L414-L423
@app.server.route("/about")
def about_page():
    return dashboard.elements.ABOUT_PAGE


# ------------------------ app layout -------------------------------    

"""
NOTE: Objects from dash_mantine_components (dmc) fail to render
      while not using dmc.MantineProvider.
"""
app.layout = dmc.MantineProvider(
    html.Div([
        dashboard.elements.navbar,
        html.Div([
                #dashboard.bars.sidebar,
                #dash.page_container,
                dashboard.elements.model_selection,
                dashboard.elements.chatbox
            ],
            className="content"
        ),
    ])
)


# ------------------------ callbacks --------------------------------

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


@callback(
    Output("chat-history", "children"),
    Output("input-textarea", "value"),
    Output("loading-button", "loading"),
    State("chat-history", "children"),
    State("input-textarea", "value"),
    Input("loading-button", "n_clicks"),
    prevent_initial_call=True,
)
def add_chat_card(chat_history, input_text, n_clicks):
    #if input_text is None or input_text == "":
    #    raise dash.exceptions.PreventUpdate
    
    # check input text
    print(f'# Input to be passed to vllm-server: {input_text}')
    if input_text is None or input_text == "":
        print(f'# Invalid input text: {input_text}.')
        response_text = "Unable to generate a resonse."
    else:
        # post request to vllm-server
        reposnse = vllm_connector.ask(input_text)
        response_text = ''.join(str(chunk) for chunk in reposnse)
        print(f'# Output recived from vllm-server: {reposnse}\n')
    
    # create new bubbles
    user_card = dashboard.elements.generate_user_bubble(input_text)
    ai_card = dashboard.elements.generate_ai_bubble(response_text)
    
    # update chat
    chat_history.append(user_card)
    chat_history.append(ai_card)

    return chat_history, "", False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8050)
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--vllm_host", type=str, default="http://10.0.1.3:8000/v1")
    args = parser.parse_args()
    
    vllm_api_url = args.vllm_host
    if "http" not in vllm_api_url:
        vllm_api_url = "http://" + vllm_api_url
    
    print(f'# Connecting to vLLM server at {vllm_api_url}')
    if vllm_connector is None:
        vllm_connector = client.vllm_connector.vllmConnector(
            vllm_api_url, 
            api_key="EMPTY"
        )
    print(f'# Using model: {vllm_connector.model}')
    print()
    
    app.run(
        debug=args.debug,
        host=args.host,
        port=args.port,
    )

