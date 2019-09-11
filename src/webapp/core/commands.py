import pytest
from flask_script import Command

# deprecated in favor of webapp.core.commands.test

class PytestCommand(Command):
    """Runs tests"""
    capture_all_args = True

    def __call__(self, app=None, *args):
        pytest.main(*args)
