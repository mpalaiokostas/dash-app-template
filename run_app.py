import platform
from app.app import create_app


if __name__ == "__main__":
    if platform.system() == "Windows":
        app = create_app("Local")
        server = app.server
        app.run_server(debug=True)
