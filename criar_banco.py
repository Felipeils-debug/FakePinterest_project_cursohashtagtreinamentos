from fakepinterestcopy import database, app
from fakepinterestcopy.models import Usuario, Foto

with app.app_context():
    database.create_all()


