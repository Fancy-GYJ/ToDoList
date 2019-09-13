
from . import auth


@auth.route('/')
def auth_home():
    return 'auth_home'


@auth.route('/login')
def login():
    return 'login'


@auth.route('/logout')
def logout():
    return 'logout'
