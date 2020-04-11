import dash_html_components as html
import dash_core_components as dcc


def get_code():
    code = html.Div(
        [
            html.H1("Example Static Tab"),
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ]
    )
    return code


def get_callbacks(app):
    return None
