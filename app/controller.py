class CallbackControls:
    def __init__(self, app):
        self.app = app

    def load_tab_callbacks(self, tab_objects):
        for tab in tab_objects:
            tab.get_tab_callbacks(self.app)
