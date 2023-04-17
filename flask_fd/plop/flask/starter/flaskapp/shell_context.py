

from app.config import Config
from app import app, db


"""This shell context will be 'magically' found by flask when calling
the cli:
$ flask shell
 """

@app.shell_context_processor
def make_shell_context():
    """To be populated..."""
    context = {
    }
    return context
