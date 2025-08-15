"""montar con MYSQL potencial de empresas propias
 con su correspondiente Base de datos"""
import mysql.connector
import click
from flask import current_app , g
from flask.cli import with_appcontext
from .schema import instructions #el schema de nuestra BD
def get_db():
    """Debemos definir las variables de entorno con los comando de export
      ej: export FLASK_APP=app"""
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary= True)
    return g.db,g.c
def close_db(e=None):
    """DOC"""
    db = g.pop('db',None)
    if db is not None:
        db.close()
def init_db():
    """DOC"""
    db,c=get_db()
    for i in instructions:
        c.execute(i)
    db.commit()
@click.command('init-db')
@with_appcontext
def init_db_command():
    """DOC"""
    init_db()
    click.echo('Base de datos inicializada')
def init_app(app):
    """DOC"""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
