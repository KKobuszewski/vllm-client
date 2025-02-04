# -*- coding: utf-8 -*-

"""
Example chatbox.
Source: https://github.com/troyscribner/stocknews/blob/main/dashboard/pages/stocks/chatbox.py

stocknews.dashboard.pages.stocks.chatbox.py
---------
chatbox.py


Created : 28 December 2023
Last Modified : 28 December 2023
"""

import dash.exceptions
from dash import Input, Output, State, callback, html, dcc, clientside_callback
#import dash_ag_grid as dag
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify


def generate_user_bubble(text):

    return dbc.Card(
        dcc.Markdown(text),
        style={
        "width": "max-content",
        "font-size": "14px",
        "padding": "0px 0px",
        "border-radius": 15,
        "margin-bottom": 5,
        "margin-left": "auto",
        "margin-right": 0,
        "max-width": "80%",
    },
        body=True,
        color="#357ED5",
        inverse=True
    )


def generate_ai_bubble(text):
    return dbc.Card(
        dcc.Markdown(text),
        style={
            "width": "max-content",
            "font-size": "14px",
            "padding": "0px 0px",
            "border-radius": 15,
            "margin-bottom": 5,
            "margin-left": 0,
            "margin-right": "auto",
            "max-width": "80%",
        },
        body=True,
        color="#F5F5F5",
        inverse=False,
    )


chat_history = html.Div(
    html.Div(
        id="chat-history",
        children=[generate_ai_bubble("Enter questions in the prompt below.")]
    ),
    style={
        "overflow-y": "auto",
        "display": "flex",
        "height": "47vh",
        "flex-direction": "column-reverse",
    },
)

chatbox = dmc.Stack(
    children=[
        dmc.Select(
            id="model-select",
            data=["DeepSeek"], # <---------- TODO: here put models
            value="DeepSeek",
            style={"width": 200},
            searchable=True,
            #icon=DashIconify(icon="radix-icons:magnifying-glass"),
            rightSection=DashIconify(icon="radix-icons:chevron-down"),
        ),
        chat_history,
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
)
chatbox = dbc.Col(
    children=[chatbox],
    width=5,
    # className="g-0",
    style={}
)
chatbox = dbc.Row(children=[chatbox])


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
        user_card = generate_user_bubble(input_text)
        ai_card = generate_ai_bubble(result["output"])

    except:
        user_card = generate_user_bubble(input_text)
        ai_card = generate_ai_bubble("Unable to generate a resonse. Reenter OpenAI API Key and refresh page.")
    chat_history.append(user_card)
    chat_history.append(ai_card)

    return chat_history, "", False
