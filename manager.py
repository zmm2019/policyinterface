from flask_script import Manager
from Chat import app, db
from flask_migrate import Migrate, MigrateCommand
# from model.models import User, Message

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
