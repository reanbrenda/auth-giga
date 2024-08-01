from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from header import make_header

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div(
    style={
        'backgroundColor': '#2c2c2c',
        'height': '100vh',
        'display': 'flex',
        'flexDirection': 'column'
    },
    children=[
        make_header(),  # Header at the top
        html.Div(
            style={
                'flex': '1',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            children=[
                html.Div(
                    style={
                        'backgroundColor': '#4c4c4c',
                        'padding': '40px',
                        'borderRadius': '10px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'
                    },
                    children=[
                        html.H2('Login', style={'color': 'white', 'textAlign': 'center'}),
                        dcc.Input(
                            id='username',
                            type='text',
                            placeholder='Username',
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'margin': '10px 0',
                                'border': 'none',
                                'borderRadius': '5px'
                            }
                        ),
                        dcc.Input(
                            id='password',
                            type='password',
                            placeholder='Password',
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'margin': '10px 0',
                                'border': 'none',
                                'borderRadius': '5px'
                            }
                        ),
                        html.Button(
                            'Login',
                            id='login-button',
                            n_clicks=0,
                            style={
                                'width': '100%',
                                'padding': '10px',
                                'margin': '20px 0',
                                'border': 'none',
                                'borderRadius': '5px',
                                'backgroundColor': '#333',
                                'color': 'white',
                                'cursor': 'pointer'
                            }
                        ),
                        html.Div(id='login-output', style={'color': 'white', 'textAlign': 'center'})
                    ]
                )
            ]
        )
    ]
)

# Define the callback for login action
@callback(
    Output('login-output', 'children'),
    Input('login-button', 'n_clicks'),
    Input('username', 'value'),
    Input('password', 'value')
)
def update_output(n_clicks, username, password):
    if n_clicks > 0:
        if username == 'admin' and password == 'password':
            return 'Login Successful'
        else:
            return 'Invalid Username or Password'
    return ''

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
