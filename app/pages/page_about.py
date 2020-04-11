import dash_html_components as html
import dash_core_components as dcc


def get_code():
    instructions = """
    ## Info about the page
    """
    code = html.Div(
        [
            html.H1("About"),
            html.Div(dcc.Markdown(instructions))
        ]
    )
    return code


def get_callbacks(app):
    return None