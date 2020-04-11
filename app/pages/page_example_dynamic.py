import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def get_code():
    code = html.Div(
        [
            html.H1("Example Dynamic Tab"),
            dcc.Input(id="my-id", value="initial value", type="text"),
            html.Div(id="my-div", children=[]),
        ]
    )
    return code


def get_callbacks(app):

    # List all your callbacks here
    @app.callback(Output("my-div", "children"), [Input("my-id", "value")])
    def update_output_div(input_value):
        return 'You\'ve entered "{}"'.format(input_value)

    return None
