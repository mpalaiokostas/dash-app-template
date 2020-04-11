import dash_html_components as html
import dash_core_components as dcc
import base64


class AppLayout:
    def __init__(self, title, subtitle, logo, mail, footer_text, mail_subject, user_tabs):
        self.title = title
        self.subtitle = subtitle
        self.logo = logo
        self.mail = mail
        self.footer_text = footer_text
        self.mail_subject = mail_subject
        self.user_tabs = user_tabs

    def create_layout(self):
        self.layout = html.Div(
            className="container page-layout",
            children=[
                self.add_header(),
                self.get_tabs(),
                self.add_footer(),
            ],
        )

    def add_header(self):
        # TODO Add exception for when there is no logo. 
        code = html.Div(
            className='container-fluid header',
            children=[
                html.Div(
                    className='row',
                    children=[
                        html.Div(
                            className='col-lg-3 col-md-3',
                            style={
                                'textAlign': 'left'
                            },
                            children=[
                                html.Img(
                                    id='logo',
                                    src='data:image/png;base64,{}'.format(
                                        base64.b64encode(open(self.logo, 'rb').read()).decode()
                                    )
                                )
                            ]
                        ),
                        html.Div(
                            className='col-lg-8 col-md-8',
                            children=[
                                html.Br(),
                                html.H2(html.B(self.title)),
                                html.H5(html.B(self.subtitle)),
                            ]
                        )
                    ]
                )
            ]
        )
        return code

    def get_tabs(self):
        return html.Div(
            className="tab-main",
            children=[
                html.Br(),
                html.Div(
                    className='container-fluid',
                    children=[
                        dcc.Tabs(
                            id="tabs-container",
                            value=self.user_tabs[0].get_tab_id(),
                            parent_className='custom-tabs',
                            className='custom-tabs-container',
                            children=[
                                dcc.Tab(
                                    label=tab.get_tab_title(),
                                    value=tab.get_tab_id(),
                                    children=tab.get_tab_code(),
                                    className='custom-tab',
                                    selected_className='custom-tab--selected'
                                )
                                for i, tab in enumerate(self.user_tabs)
                            ],
                        )
                    ]
                ),
                html.Br(),
                html.Div(className='container-fluid', id='tabs-contents'),
                html.Br()

            ]
        )

    def add_footer(self):
        code = html.Div(
            className='container-fluid footer',
            children=[
                html.Br(),
                html.H6(html.P(self.footer_text)),
                html.H6(html.A('Get in contact', href=self.mail_subject, target="_top")),
                html.Br()
            ]
        )
        return code
