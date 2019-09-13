from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app import create_app, db

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


@manager.command
def test():
   """Run the unit tests."""
   import unittest
   tests = unittest.TestLoader().discover('tests')
   unittest.TextTestRunner(verbosity=2).run(tests)

# 初始化 Flask-Script、Flask-Migrate 和为 Python shell 定义的上下文。
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
