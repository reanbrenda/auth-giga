from dash import html, dcc

def make_header() -> html.Header:
    return html.Header(
        children=[
            # Icon and title container
            html.Div(
                className="dash-title-container",
                children=[
                    html.A(  # Wrap the image in an anchor tag (A)
                        href="https://giga.global/",  # Replace with your desired URL
                        target="_blank",  # Open the link in a new tab
                        children=[
                            html.Img(className="dash-icon", src="assets/img/GIGA_lockup_white_horizontal.png", width=300, style={"padding-top": "10px"})
                        ],
                    ),
                    html.H1(className="dash-title", children=['AI School Mapping Validator']),
                ],
            ),
            # create navigator with buttons
            html.Nav(
                children=[
                    dcc.Tabs(
                        id="navigation-tabs",
                        value="tab-tool",
                        children=[
                            dcc.Tab(
                                label='Validator',
                                value="tab-tool",
                                className="dash-tab",
                                selected_className="dash-tab-selected",
                            ),
                            dcc.Tab(
                                label='About',
                                value="tab-about",
                                className="dash-tab",
                                selected_className="dash-tab-selected",
                            ),
                        ],
                    ),
                ]
            ),
        ]
    )
