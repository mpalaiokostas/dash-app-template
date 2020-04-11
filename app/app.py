import dash
import os

from app.constants import Constants
from app.controller import CallbackControls
from app.view import AppLayout
from app.user_content import UserContent


def create_app(platform_):

    # Load user settings and components
    user = UserContent()
    user_settings = user.get_user_settings()
    user_tabs = user.load_user_tabs()

    conf = Constants(
        user_settings["app_title"],
        user_settings["app_subtitle"],
        user_settings["contact_email"],
    )

    page_layout = AppLayout(
        conf.APP_TITLE,
        conf.APP_SUBTITLE,
        conf.PATH_LOGO,
        conf.EMAIL,
        conf.FOOTER_TEXT,
        conf.CONTACT_MAIL_SUBJECT,
        user_tabs,
    )
    page_layout.create_layout()

    # Create the app instance
    external_stylesheets = [
        'https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css',
    ]

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.title = conf.APP_TITLE
    app.config.suppress_callback_exceptions = True
    if platform_ == "local":
        requests_prefix = ''
        app.config.update({'requests_pathname_prefix': requests_prefix})
    else:
        requests_prefix = ''
    app.layout = page_layout.layout
    cc = CallbackControls(app)
    cc.load_tab_callbacks(user_tabs)
    return app
