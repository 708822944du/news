from flask import Flask
from config import config_dict
from info.admin.admin import admin_blue
from info.news.news import news_blue
from info.news.user import user_blue
from flask_wtf import CSRFProtect
from models import db
#迁移
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from apps import app

manage = Manager(app)
migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)
#跨站攻击
CSRFProtect(app)
#注册蓝图
app.register_blueprint(admin_blue,url_prefix="/admin")
#注册首页蓝图
app.register_blueprint(news_blue)
#注册用户蓝图
app.register_blueprint(user_blue,url_prefix="/user")


if __name__ == "__main__":
    # manage.run()
    app.run()