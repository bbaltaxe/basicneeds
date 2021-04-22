# Server README

## To run background server

1. First ensure you have 2 seperate terminals; one dedicated for the client and one the server.
2. Navigate to the mgflask folder

    ```sh
    $ cd basicneeds/server/
    ```

3. Create and activate Python Virtual Environment

    ```sh
    $ python3 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    ```

4. Start up flask environment with the following commands

    ```sh
    (env)$ export FLASK_APP=webapp
    (env)$ export FLASK_ENV=development
    (env)$ flask run
    ```

## Register new module

 1.   Within the init.py in the def create_app() import the module and call app.register_blueprint. 
For example, if you have a folder foo/ with bar.py

```
src/
├── README.md
├── instance
│   └── basicneeds.sqlite
└── webapp
    ├── __init__.py
    ├── auth.py
    ├── db.py
    ├── metadata.txt
    ├── schema.sql
    ├── services
    │   └── admin.py
    └── static_pages
        └── campus.py
    |  ...

```

\_\_init_\_.py
```
from .foo import bar

def create_app():
 
    ... 
    app.register_blueprint(foo.bp)
    ...
```
 2.   In foo/bar.py add this line

foo/bar.py

```
...
bp = Blueprint('bar', __name__)
...
```

## Database

To init or reset the database call within basicneeds/server/src/webapp

 >  flask init-db
