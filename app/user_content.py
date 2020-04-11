from app.view_components import Tab
from app.pages import page_about, page_example_static, page_example_dynamic


class UserContent:
    def get_user_settings(self):
        return {
            "app_title": "example title",
            "app_subtitle": "example subtitle",
            "contact_email": "dev@dev.com",
        }

    def load_user_tabs(self):
        return [
            Tab(
                title="Static page",
                id="tab-static-page",
                html_code=page_example_static.get_code(),
                callbacks=page_example_static.get_callbacks,
            ),
            Tab(
                title="Dynamic page",
                id="tab-dynamic-page",
                html_code=page_example_dynamic.get_code(),
                callbacks=page_example_dynamic.get_callbacks,
            ),
            Tab(
                title="About",
                id="tab-about",
                html_code=page_about.get_code(),
                callbacks=page_about.get_callbacks,
            ),
        ]
