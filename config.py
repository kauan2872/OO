from dynaconf import FlaskDynaconf
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def configure(app):
    FlaskDynaconf(app, extensions_list='Extensions', root_path=HERE)
