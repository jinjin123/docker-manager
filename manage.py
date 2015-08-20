from flask.ext.script import Manager
from docker_manager.config import config_loader
from docker_manager import app
from docker_manager.commands import Prerequisites

manager = Manager(app)
config_loader(app)

if __name__ == '__main__':
    manager.add_command('prerequisites', Prerequisites(app=app))
    manager.run()

