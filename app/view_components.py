class Tab:
    def __init__(self, title, id, html_code, callbacks):
        self.title = title
        self.id = id
        self.html_code = html_code
        self.callbacks = callbacks

    def get_tab_title(self):
        return self.title

    def get_tab_code(self):
        return self.html_code

    def get_tab_id(self):
        return self.id

    def get_tab_callbacks(self, app):
        return self.callbacks(app)
