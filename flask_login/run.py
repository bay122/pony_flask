from app import app
from views import *
'''
docs: https://j2logo.com/tutorial-flask-leccion-4-login/
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins/page/6
https://docs.ponyorm.org/integration_with_flask.html
'''
if __name__ == '__main__':
    db.bind(**app.config['PONY'])
    db.generate_mapping(create_tables=True)
    app.run()