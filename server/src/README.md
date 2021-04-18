Server README
To run background server

First ensure you have 2 seperate terminals; one dedicated for the client and one the server.
Prerequisies to running server for development

    export FLASK_APP=webapp

    export FLASK_ENV=development

Running the server in development mode

    Within the folder

    basicneeds/server/src/webapp

    Run the command

    flask run

Register new modulle

    Within the

    init.py in the def create_app() import the module and call app.register_blueprint For example, if you have a folder foo/ with bar.py

__init__.py

    from .foo import bar

    def create_app():

    ...

    app.register_blueprint(foo.bp)

    ...

    In foo/bar.py add this line

foo/bar.py

    bp = Blueprint('bar', __name__)

Database

    To init or reset the database call within basicneeds/server/src/webapp

    flask init-db
