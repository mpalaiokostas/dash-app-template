import os


class Constants:
    def __init__(self, title, subtitle, email):
        """Change at your peril"""
        self.DIR_DATA_STORE = "results"
        self.DIR_SETTINGS = "settings"
        self.DIR_STATIC = "/static/"
        self.DIR_APP = os.path.abspath(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
        )
        self.PATH_LOGO = os.path.join(
            self.DIR_APP, "app", "assets", "images", "template_logo_200x200.png"
        )
        self.FOOTER_TEXT = ""

        self.APP_TITLE = title
        self.APP_SUBTITLE = subtitle
        self.EMAIL = email
        self.CONTACT_MAIL_SUBJECT = f"mailto:{self.EMAIL}?Subject=[{self.APP_TITLE}] Support"
