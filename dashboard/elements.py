# -*- coding: utf-8 -*-

"""
Elements of chatbox website.
Source: https://github.com/troyscribner/stocknews/blob/main/dashboard/pages/stocks/chatbox.py

stocknews.dashboard.pages.stocks.chatbox.py
---------
chatbox.py


Created : 28 December 2023
Last Modified : 28 December 2023
"""

from dash import html, dcc
#import dash_ag_grid as dag
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify


# NOTE: Static webpage can be provided like below
ABOUT_PAGE = f'''
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
#ABOUT_PAGE = dcc.Markdown(''' some content of webpage ''')


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
        dcc.Markdown(text), # <---------- TODO: Probably somewhere here is problem with too high buble
        style={
            "width": "max-content",
            "font-size": "14px",
            "padding": "0px 0px",
            "border-radius": 15,
            "margin-bottom": 1,
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
        # NOTE: More bubbles will be added by callback `add_chat_card`
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
    style={
        "height": "60vh",
        "margin-left": "5%",
        "margin-right": "5%",
        "justify-content": "center"
    },
)

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
        dbc.NavItem(dbc.NavLink("About", id="about", href="/about", external_link=True), ),
        #dbc.NavItem(dbc.NavLink("About", id="about", href="/about"), ), # NOTE: still not working
    ],
    brand="vLLM Chat",
    brand_href="#",
    color="primary",
    dark=True,
    style={"margin": 0, "height": "7vh",},
    id="navbar"
)

model_selection = dmc.Select(
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
)
