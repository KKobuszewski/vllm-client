# -*- coding: utf-8 -*-

"""
"""
import argparse

from flask import Flask, jsonify
import dash
import dash.exceptions
from dash import Dash
from dash import DiskcacheManager, CeleryManager, Input, Output, State, \
                 clientside_callback, callback, html, dcc, _dash_renderer
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

import dashboard
import dashboard.elements

# import system variables
import dotenv
dotenv.load_dotenv()

_dash_renderer._set_react_version("18.2.0")

# create Flask & Dash server
server = Flask(__name__)
app = Dash(
    'vllm-chat',#__name__,
    server = server,
    external_stylesheets=[dbc.themes.SANDSTONE, dbc.icons. FONT_AWESOME] + dmc.styles.ALL,
    #use_pages=True,
    #pages_folder="pages",
    #assets_folder="dashboard/assets",
    #requests_pathname_prefix='/dashboard/'
)
app.title = "vllm-chat"
#app.config.suppress_callback_exceptions = True

#server = app.server


# ------------------------ endpoints --------------------------------

# NOTE: There's probably another way do add endpoint to Dash app
#view_func = lambda x : 
#app._add_url('', view_func, methods=('GET',))

# TODO: Model selection (dashboard.elements.model_selection) not working properly.
# TODO: In dashboard.elements.navbar NavLink does not connect to
#       about page while clicked.
@server.route("/about")
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
    
    print(f'input to be passed to vllm: {input_text}\n')
    
    # here post request to vllm-server
    #global agent

    try:
        #result = agent({"input": input_text})
        result = {"output" : "dummy output"}
        
        # # create the users prompt card
        user_card = dashboard.elements.generate_user_bubble(input_text)
        ai_card = dashboard.elements.generate_ai_bubble(result["output"])

    except:
        user_card = generate_user_bubble(input_text)
        ai_card = generate_ai_bubble("Unable to generate a resonse.")
    chat_history.append(user_card)
    chat_history.append(ai_card)

    return chat_history, "", False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8050)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    
    app.run(
        debug=args.debug,
        host=args.host,
        port=args.port,
    )

