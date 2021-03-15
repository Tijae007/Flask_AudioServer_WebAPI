import os
import time
from datetime import datetime

from flask_migrate import init, migrate, revision, upgrade, current, downgrade

from audio import app


class Usable(object):
    def __init__(self):
        self.time = datetime.utcfromtimestamp(time.time())
        self.directory = os.path.join(os.getcwd(), 'migrations', 'versions')

    def message(self):
        return self.time.strftime("%Y_%m_%d")

    def revision_id(self):
        path, dirs, files = next(os.walk(self.directory))
        return str(len([file_ for file_ in files if file_.endswith('.py')]) + 1).zfill(6)


@app.cli.command("dbi")
def dbi():
    """
    Calls the init()
    :return: None
    """
    init()


@app.cli.command("dbm")
def dbm():
    """
    Calls the migrate()
    :return: None
    """
    usable = Usable()
    migrate(message=usable.message(), rev_id=usable.revision_id())


@app.cli.command("dbr")
def dbr():
    """
    Calls the revision()
    :return: None
    """
    usable = Usable()
    revision(message=usable.message(), rev_id=usable.revision_id())


@app.cli.command("dbu-sql")
def dbu_sql():
    """
    Generate SQL statements but you will personally have to `run` it on your DB
    :return: None
    """
    upgrade(sql=True)


@app.cli.command("dbc")
def db_current():
    """
    Calls the current()
    :return: None
    """
    current()


@app.cli.command("dbu-no-sql")
def dbu_no_sql():
    """
    Bring the DB up to date with your data models.
    Calls the migrate()
    :return: None
    """
    upgrade()


@app.cli.command("dd-sql")
def downgrade_sql():
    """
    Generate SQL statements but you will personally have to `run` it on your DB
    :return: None
    """
    downgrade(sql=True)


@app.cli.command("dd-no-sql")
def downgrade_no_sql():
    """
    Bring the DB up to date with your data models.
    Calls the downgrade()
    :return: None
    """
    downgrade()

