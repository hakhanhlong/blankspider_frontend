from app import create_app
from flask.ext.script import Manager, Shell, Server
import os

app = create_app(os.getenv('BLANKSPIDER_EVR') or 'default')
manager = Manager(app)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response



manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port='8066'))

if __name__ == '__main__':
    manager.run()