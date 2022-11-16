from flask import Flask

__all__ = ["init_app"]

DEFAULT_APP_NAME = "flask_ddd_example"


def init_app(app_name: str = None):

    if app_name is None:
        app_name = DEFAULT_APP_NAME

    _app = Flask(app_name)

    return _app


if __name__ == '__main__':
    app = init_app()
